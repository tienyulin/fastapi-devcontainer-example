# FastAPI DevContainer Example

## Quick Start

1. Open in VS Code with DevContainer extension
2. Press `Cmd+Shift+P` → "Dev Containers: Reopen in Container"
3. API runs at http://localhost:8000
4. Docs at http://localhost:8000/docs

## Run locally (without DevContainer)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
