# ATS Resume Matcher

A full-stack web application that analyzes how well a resume matches a job description using keyword-based ATS (Applicant Tracking System) logic.

The project focuses on core ATS analysis, clean backend architecture, and a simple, usable frontend.

## 🚀 Features

- Paste resume text and job description
- Automatically extracts keywords
- Calculates match percentage
- Shows matched and missing keywords
- Handles edge cases (empty input, stop-word-only text)
- Clean frontend + REST API backend
- CORS-safe and production-ready logic

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Backend
- Python
- FastAPI
- scikit-learn
- Uvicorn

## 🧠 How It Works

1. User pastes resume text and job description in the UI
2. Frontend sends data to FastAPI backend
3. Backend:
   - Cleans text
   - Removes stop words
   - Extracts keywords using CountVectorizer
   - Compares resume vs job description
4. Backend returns:
   - Match percentage
   - Matched keywords
   - Missing keywords
5. Frontend displays the result in a readable format

## 📂 Project Structure

```
ats-resume-matcher/
├── backend/
│   ├── main.py          # FastAPI app & API routes
│   ├── matcher.py       # ATS keyword matching logic
│   ├── requirements.txt
│   └── venv/            # (ignored in git)
│
├── frontend/
│   ├── index.html       # UI
│   ├── style.css        # Styling
│   └── script.js        # Frontend logic
│
├── .gitignore
└── README.md
```

## ▶️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/anonymous243/ats-resume-matcher.git
cd ats-resume-matcher
```

### 2. Backend setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

**Backend runs at:**
- http://127.0.0.1:8000

**API docs:**
- http://127.0.0.1:8000/docs

### 3. Frontend

Open `frontend/index.html` in your browser.

## ⚠️ Limitations (Intentional)

- Resume content is pasted as text (no PDF/DOC upload yet)
- Keyword-based matching (not semantic embeddings)

These were intentionally kept out of scope to focus on core ATS logic.

## License
This project is licensed under the MIT License.

