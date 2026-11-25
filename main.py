"""Offline study task planner."""
import argparse, sqlite3
from datetime import date
from pathlib import Path
DB=Path(__file__).with_name("study.db")

def db():
    c=sqlite3.connect(DB); c.row_factory=sqlite3.Row
    c.execute("""CREATE TABLE IF NOT EXISTS tasks(
      id INTEGER PRIMARY KEY, subject TEXT NOT NULL, task TEXT NOT NULL,
      due TEXT, done INTEGER NOT NULL DEFAULT 0)""")
    return c

def main():
    p=argparse.ArgumentParser(description="Plan study tasks.")
    s=p.add_subparsers(dest="cmd",required=True)
    a=s.add_parser("add"); a.add_argument("--subject",required=True); a.add_argument("--task",required=True); a.add_argument("--due")
    d=s.add_parser("done"); d.add_argument("id",type=int)
    s.add_parser("list")
    x=p.parse_args()
    if x.cmd=="add" and x.due:
        try: date.fromisoformat(x.due)
        except ValueError: p.error("--due must use YYYY-MM-DD")
    with db() as c:
        if x.cmd=="add":
            cur=c.execute("INSERT INTO tasks(subject,task,due) VALUES(?,?,?)",(x.subject,x.task,x.due))
            print(f"Added task #{cur.lastrowid}.")
        elif x.cmd=="done":
            cur=c.execute("UPDATE tasks SET done=1 WHERE id=?",(x.id,))
            print("Marked complete." if cur.rowcount else "Task not found.")
        else:
            rows=c.execute("SELECT * FROM tasks ORDER BY done,due IS NULL,due,id").fetchall()
            for r in rows: print(f"[{'x' if r['done'] else ' '}] #{r['id']} {r['subject']}: {r['task']} (due {r['due'] or 'not set'})")
            if not rows: print("No study tasks yet.")
if __name__=="__main__": main()
