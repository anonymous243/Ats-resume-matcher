from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from matcher import analyze_resume

app = FastAPI()

# ✅ CORS MUST be added immediately after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for local + demo
    allow_methods=["*"],   # IMPORTANT: allows OPTIONS, POST, GET
    allow_headers=["*"],
    allow_credentials=False,
)


class ResumeRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def root():
    return {"status": "ATS Backend is running"}


@app.post("/analyze")
def analyze(request: ResumeRequest):
    return analyze_resume(
        request.resume_text,
        request.job_description
    )
