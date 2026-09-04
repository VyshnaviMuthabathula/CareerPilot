def generate_interview_questions(target_role: str, skills: list[str]) -> dict:
    """
    Generate interview preparation questions for a target internship.
    """

    target_role = target_role.strip()

    if not target_role:
        return {
            "success": False,
            "message": "Please provide a target internship role."
        }

    if not skills:
        return {
            "success": False,
            "message": "Please provide at least one skill."
        }

    questions = [
        f"Tell me about yourself and why you are interested in the {target_role} role.",
        f"Why do you want to work as a {target_role}?",
        "What project are you most proud of and what did you learn from it?",
        "Describe a technical problem you faced and how you solved it.",
        "How do you learn a new technology or technical concept?"
    ]

    skill_questions = []

    for skill in skills:
        skill_questions.append(
            f"What is your experience with {skill}, and how have you used it in a project?"
        )

    return {
        "success": True,
        "target_role": target_role,
        "skills": skills,
        "general_questions": questions,
        "skill_based_questions": skill_questions
    }