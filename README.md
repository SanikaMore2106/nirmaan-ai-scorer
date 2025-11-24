<<<<<<< HEAD
# nirmaan-ai-scorer
=======
# Nirmaan AI Intern Case Study — Transcript Scoring Tool

This tool evaluates a student’s self-introduction transcript using:
✔ Rule-based scoring  
✔ NLP semantic similarity  
✔ Rubric-based weighted scoring  

## Features
- Keyword detection
- Word count evaluation
- Semantic similarity (MiniLM Transformer model)
- Per-criterion feedback
- Overall score (0–100)
- Simple frontend UI

## Folder Structure
(Include the folder structure above)

## How to Run Backend
cd backend  
pip install -r requirements.txt  
uvicorn app:app --reload --port 8000  

## How to Run Frontend
Open frontend/index.html in a browser

Make sure backend is running at:
http://127.0.0.1:8000/score

## API Endpoint
POST /score  
Body:
{
  "transcript": "student introduction text"
}

## Output
- overall_score
- per-criterion feedback
- semantic score
- keyword score
- length score
>>>>>>> af848f1f (Initial commit - Added full project)
