import PyPDF2

SKILLS = [
    "python", "java", "sql", "machine learning",
    "ai", "django", "react", "node", "data"
]

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

def calculate_score(text):
    score = 0
    matched = []

    for skill in SKILLS:
        if skill in text:
            score += 10
            matched.append(skill)

    return min(score, 100), matched
