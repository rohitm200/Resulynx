from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2

def extract_text(file):
    try:
        file.seek(0)
    except Exception:
        pass
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()


def match_score(resume_text, job_text):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return int(score * 100)
