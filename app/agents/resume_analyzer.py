def analyze_resume(resume_text: str) -> dict:
    """
    Analyze resume text and identify relevant skills.
    """

    resume_text = resume_text.strip()

    if not resume_text:
        return {
            "success": False,
            "message": "Please provide resume text."
        }

    text_lower = resume_text.lower()

    skill_keywords = {
        "Python": ["python"],
        "Machine Learning": ["machine learning", "ml"],
        "Artificial Intelligence": ["artificial intelligence", "ai"],
        "JavaScript": ["javascript"],
        "React": ["react"],
        "HTML": ["html"],
        "CSS": ["css"],
        "SQL": ["sql"],
        "Java": [" java "],
        "Git": ["git", "github"]
    }

    detected_skills = []

    for skill, keywords in skill_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_skills.append(skill)

    return {
        "success": True,
        "skills_detected": detected_skills,
        "skill_count": len(detected_skills)
    }