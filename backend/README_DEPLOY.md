1. Place trained model files into backend/models/:
- resume_score_model.joblib
- resume_tfidf.joblib
- skills_ontology.json
- interview_text_model.joblib
- interview_tfidf.joblib


2. Commit & push repo to your fork.


3. On Render: Create a new Web Service -> connect repo -> choose the backend folder.
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn -k uvicorn.workers.UvicornWorker main:app`


4. Set environment variable MODEL_DIR if you use a different path.
