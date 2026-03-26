# 🧠 HIREHEAD – AI Resume & Interview Assistant

AI-powered platform that analyzes resumes, evaluates interview answers, and provides personalized improvement suggestions.

This project includes:

- **Resume Bot** – ATS-style resume scoring + skill gap analysis  
- **Interview Bot** – NLP scoring of interview answers  
- **Next.js Frontend** – User-friendly UI  
- **FastAPI Backend** – Hosts and serves ML models  
- **Deployable on Render (Free Tier)**  

---

## 🚀 Features

### ✔ Resume Bot
- Scores resumes on a 1–10 scale  
- Detects missing skills and keywords  
- Simple & fast ML pipeline (TF-IDF + RandomForest)  
- Works with plain text input  

### ✔ Interview Bot
- Scores interview responses (clarity, completeness)  
- Fast NLP scoring using TF-IDF + RandomForest  
- Lightweight and deployable on Render free tier  

### ✔ Frontend (Next.js)
- Clean input UI  
- Real-time API calls  
- Central proxy route to communicate with backend  

### ✔ Backend (FastAPI)
- REST APIs  
- Loads joblib ML models  
- Fast inference  
- Supports CORS & environment variables  

---

## 📁 Project Structure

```
hireHEAD/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   ├── Procfile
│   ├── README_DEPLOY.md
│   ├── models/
│   │   ├── resume_score_model.joblib
│   │   ├── resume_tfidf.joblib
│   │   ├── skills_ontology.json
│   │   ├── interview_text_model.joblib
│   │   └── interview_tfidf.joblib
│
├── frontend/
│   ├── package.json
│   ├── next.config.js
│   ├── pages/
│   │   ├── index.js
│   │   └── api/proxy.js
│   └── README_DEPLOY.md
│
├── colab_notebooks/
│   └── hireHEAD_combined_safe.ipynb
│
└── README.md
```

---

## 🛠️ Tech Stack

**ML Models**
- scikit-learn  
- numpy  
- pandas  
- joblib  

**Backend**
- FastAPI  
- Uvicorn  
- Gunicorn  

**Frontend**
- Next.js  
- React  

**Deployment**
- Render Web Services  

---

## 🎓 Model Training (Google Colab)

Training performed using:

```
colab_notebooks/hireHEAD_combined_safe.ipynb
```

The notebook:
- Generates synthetic data  
- Trains Resume Bot  
- Trains Interview Bot  
- Saves all models (`joblib`)  
- Models are placed into:

```
backend/models/
```

---

## 🔌 Backend API Endpoints

### Health Check
```
GET /health
```

### Resume Scoring
```
POST /predict_resume
{
  "text": "Paste your resume here..."
}
```

### Interview Answer Scoring
```
POST /score_answer
{
  "answer": "Your interview response..."
}
```

### Example Output
```json
{
  "score": 8.2,
  "suggestions": ["AWS", "Docker", "Leadership"]
}
```

---

## 🌐 Frontend Workflow

1. User enters resume or interview answer  
2. Request sent to `/api/proxy`  
3. Proxy forwards to backend  
4. Backend returns score + suggestions  
5. UI displays results  

---

## ☁️ Deployment (Render)

### Backend (Python)
- **Build Command**
```
pip install -r requirements.txt
```
- **Start Command**
```
gunicorn -k uvicorn.workers.UvicornWorker main:app
```

### Frontend (Node.js)
- **Build Command**
```
npm install && npm run build
```
- **Start Command**
```
npm start
```

### Environment Variable
```
BACKEND_URL = https://your-backend.onrender.com
```

---

## 📐 System Architecture

```
USER
  │
  ▼
FRONTEND (Next.js)
  │
  ▼
API PROXY (/api/proxy)
  │
  ▼
BACKEND (FastAPI)
  │
  ├── Resume TF-IDF Model
  └── Interview TF-IDF Model
```

---

## 🔮 Future Enhancements

- Audio-based confidence scoring  
- Video-based body language detection  
- ATS resume parsing from PDFs  
- Mock AI interviewer  
- Job recommendation system  

---

## 👩‍💻 Author

Sami Noor Saifi
