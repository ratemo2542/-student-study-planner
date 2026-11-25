# Student Study Planner

An offline study planner with a Python/SQLite command-line tool and a separate browser dashboard. The CLI stores tasks in `study.db`; the browser dashboard stores its own tasks in this browser's localStorage.

## CLI requirements
- Python 3.10+
- No third-party packages

## CLI usage
```bash
python main.py add --subject "Quantitative Methods" --task "Revise probability" --due 2026-12-01
python main.py list
python main.py done 1
```

Dates use YYYY-MM-DD. Run `python main.py --help` for command details.

## Browser dashboard
Open `index.html` in a browser. It is a separate local-only interface and does not sync with the SQLite CLI or other devices.

## Security and scope
This is a personal offline planner, not a hosted multi-user service. Browser data is stored locally and can be removed by clearing browser storage.
