def generate_application_materials(goal: str, skills: list[str], target_role: str) -> dict:
    """
    Generate customized application material for an internship.
    """

    goal = goal.strip()
    target_role = target_role.strip()

    if not goal:
        return {
            "success": False,
            "message": "Please provide a career goal."
        }

    if not skills:
        return {
            "success": False,
            "message": "Please provide at least one skill."
        }

    if not target_role:
        return {
            "success": False,
            "message": "Please provide a target internship role."
        }

    skills_text = ", ".join(skills)

    resume_points = [
        f"Highlight your experience with {skills_text}.",
        f"Showcase projects related to {goal}.",
        f"Emphasize practical skills relevant to the {target_role} role.",
        "Mention measurable results and achievements from your projects."
    ]

    cover_letter = (
        f"I am interested in the {target_role} opportunity because "
        f"it closely matches my career goal of {goal}. "
        f"I have developed skills in {skills_text} and have worked on "
        f"projects that helped me strengthen my technical abilities. "
        f"I am eager to apply my knowledge, learn from experienced "
        f"professionals, and contribute to your team."
    )

    tell_me_about_yourself = (
        f"I am a student interested in {goal}. "
        f"My technical skills include {skills_text}. "
        f"I enjoy building practical projects and solving problems "
        f"using technology. I am currently looking for an opportunity "
        f"as a {target_role} where I can apply my skills and continue learning."
    )

    why_interested = (
        f"I am interested in this {target_role} because it aligns with "
        f"my career goal of {goal}. I believe this opportunity will allow "
        f"me to apply my existing skills while gaining practical industry "
        f"experience and learning from a professional team."
    )

    return {
        "success": True,
        "target_role": target_role,
        "career_goal": goal,
        "skills": skills,
        "resume_improvement_points": resume_points,
        "cover_letter": cover_letter,
        "tell_me_about_yourself": tell_me_about_yourself,
        "why_interested": why_interested
    }