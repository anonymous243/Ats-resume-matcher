import re
from sklearn.feature_extraction.text import CountVectorizer


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text


def analyze_resume(resume_text: str, jd_text: str) -> dict:
   
    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    # Safety check
    if not resume_text.strip() or not jd_text.strip():
        return {
            "match_percentage": 0.0,
            "matched_keywords": [],
            "missing_keywords": [],
            "message": "Resume text and Job Description must contain meaningful words."
        }

    vectorizer = CountVectorizer(stop_words="english")

    try:
        vectors = vectorizer.fit_transform([resume_text, jd_text])
    except ValueError:
        return {
            "match_percentage": 0.0,
            "matched_keywords": [],
            "missing_keywords": [],
            "message": "Not enough meaningful keywords to perform ATS analysis."
        }

    resume_vector = vectors.toarray()[0]
    jd_vector = vectors.toarray()[1]

    keywords = vectorizer.get_feature_names_out()

    matched = []
    missing = []

    for idx, word in enumerate(keywords):
        if jd_vector[idx] > 0:
            if resume_vector[idx] > 0:
                matched.append(word)
            else:
                missing.append(word)

    match_percentage = (
        len(matched) / len(keywords) * 100 if len(keywords) > 0 else 0
    )

    return {
        "match_percentage": round(match_percentage, 2),
        "matched_keywords": matched,
        "missing_keywords": missing,
    }
