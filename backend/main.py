
from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
import joblib, json, os
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app = FastAPI(title="hireHEAD-models-api")

# Models are expected in ./models/ inside the backend repo (commit them or add via release)
MODEL_DIR = os.getenv('MODEL_DIR', 'models')

# helper to load safely
def load_model(path):
    full = os.path.join(MODEL_DIR, path)
    if not os.path.exists(full):
        raise FileNotFoundError(f"Model file not found: {full}")
    return joblib.load(full)

# Load models & vectorizers
try:
    resume_vec = load_model('resume_tfidf.joblib')
    resume_model = load_model('resume_score_model.joblib')
    with open(os.path.join(MODEL_DIR, 'skills_ontology.json'),'r') as f:
        skills_ontology = json.load(f)
except Exception as e:
    # If running before models exist, don't crash — provide helpful error on health check
    resume_vec = None
    resume_model = None
    skills_ontology = []
    load_error = str(e)
else:
    load_error = ''

try:
    interview_vec = load_model('interview_tfidf.joblib')
    interview_model = load_model('interview_text_model.joblib')
except Exception as e:
    interview_vec = None
    interview_model = None
    load_error = load_error + '; ' + str(e)

class ResumeText(BaseModel):
    text: str

class AnswerText(BaseModel):
    answer: str

@app.get('/health')
def health():
    ok = resume_model is not None and interview_model is not None
    return {'status': 'ok' if ok else 'not_ready', 'load_error': load_error}

@app.post('/predict_resume')
def predict_resume(r: ResumeText):
    if resume_vec is None or resume_model is None:
        return {'error': 'models not loaded on server. Check logs or upload models to ./models'}
    X = resume_vec.transform([r.text])
    score = float(resume_model.predict(X)[0])
    # suggestions: missing skills from ontology
    present = r.text.lower()
    missing = [s for s in skills_ontology if s.lower() not in present]
    return {'score': round(score,2), 'suggestions': missing[:10]}

@app.post('/score_answer')
def score_answer(a: AnswerText):
    if interview_vec is None or interview_model is None:
        return {'error': 'interview models not loaded on server. Check logs or upload models to ./models'}
    X = interview_vec.transform([a.answer])
    score = float(interview_model.predict(X)[0])
    return {'score': round(score,2)}

# Optional endpoint to list model files
@app.get('/models_list')
def models_list():
    files = []
    if os.path.exists(MODEL_DIR):
        files = os.listdir(MODEL_DIR)
    return {'models': files}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv('PORT', 8000)))
