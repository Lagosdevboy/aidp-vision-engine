from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import requests

app = FastAPI(title="AI Market Intelligence - Backend")


class AnalyzeRequest(BaseModel):
    query: str
    data_sources: list = []
    user_id: str = None


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    """Simple analyze endpoint. If AIDP endpoint and key are configured
    it will forward the request; otherwise returns a stub response."""
    aidp_url = os.getenv("AIDP_ENDPOINT")
    api_key = os.getenv("AIDP_API_KEY")
    payload = {"query": req.query, "data_sources": req.data_sources, "user_id": req.user_id}
    if aidp_url and api_key:
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        try:
            r = requests.post(aidp_url, json=payload, headers=headers, timeout=15)
            r.raise_for_status()
            return {"status": "submitted", "aidp_response": r.json()}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return {"status": "stub", "payload": payload}
