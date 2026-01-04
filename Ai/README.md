# AI Market Intelligence (scaffold)

This repository contains a minimal scaffold for an AI Market Intelligence product:

- `backend` — FastAPI service (analysis endpoints, AIDP integration placeholders)
- `frontend` — React + Vite demo UI

Quick start

1. Backend

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

Set `AIDP_ENDPOINT` and `AIDP_API_KEY` in environment to enable forwarding to your NVIDIA AIDP.

2. Frontend

```powershell
cd frontend
npm install
npm run dev
```
