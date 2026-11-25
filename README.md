# Student Study Planner

A simple offline study planner backed by SQLite. Add study tasks, set due dates, mark work complete, and review pending tasks.

## Requirements
- Python 3.10+
- No third-party packages

## Run
```bash
python main.py add --subject "Quantitative Methods" --task "Revise probability" --due 2026-12-01
python main.py list
python main.py done 1
```

Dates use YYYY-MM-DD. Tasks are stored locally in `study.db`.
