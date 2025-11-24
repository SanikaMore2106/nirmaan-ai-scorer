from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from load_rubric import load_rubric
from scoring_logic import score_transcript

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rubric = load_rubric()

class ScoreRequest(BaseModel):
    transcript: str

@app.get("/")
def home():
    return {"message": "Backend is running!"}

@app.post("/score")
def score(req: ScoreRequest):
    text = req.transcript.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Transcript is empty")

    result = score_transcript(text, rubric)
    return result
