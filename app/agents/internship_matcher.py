def match_internships(goal: str, skills: list[str]) -> dict:
    """
    Match internships using career goal and resume skills.
    Also identifies missing skills and explains each match.
    """

    goal = goal.strip()

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

    goal_lower = goal.lower()
    skills_lower = {skill.lower() for skill in skills}

    internships = [
        {
            "role": "AI/ML Intern",
            "required_skills": {
                "python",
                "machine learning",
                "artificial intelligence"
            },
            "keywords": ["ai", "artificial intelligence", "machine learning", "ml"],
            "company_type": "AI/Technology Company"
        },
        {
            "role": "Web Development Intern",
            "required_skills": {
                "html",
                "css",
                "javascript",
                "react"
            },
            "keywords": ["web", "frontend", "full stack", "javascript"],
            "company_type": "Software Company"
        },
        {
            "role": "Data Analyst Intern",
            "required_skills": {
                "python",
                "sql"
            },
            "keywords": ["data", "analyst", "analytics"],
            "company_type": "Analytics Company"
        },
        {
            "role": "Software Development Intern",
            "required_skills": {
                "python",
                "java",
                "git"
            },
            "keywords": ["software", "developer", "programming"],
            "company_type": "Software Company"
        }
    ]

    matches = []

    for internship in internships:
        required_skills = internship["required_skills"]

        matched_skills = skills_lower.intersection(required_skills)

        missing_skills = required_skills - skills_lower

        skill_score = (
            len(matched_skills) / len(required_skills)
        ) * 70

        goal_match = any(
            keyword in goal_lower
            for keyword in internship["keywords"]
        )

        goal_score = 30 if goal_match else 0

        total_score = round(skill_score + goal_score)

        if goal_match and matched_skills:
            reason = (
                f"Your career goal matches this role and you have "
                f"{len(matched_skills)} relevant skill(s)."
            )
        elif goal_match:
            reason = "Your career goal matches this role."
        elif matched_skills:
            reason = (
                f"You have {len(matched_skills)} relevant skill(s), "
                "but your stated career goal is less directly aligned."
            )
        else:
            reason = "Your current skills have limited overlap with this role."

        matches.append({
            "role": internship["role"],
            "company_type": internship["company_type"],
            "match_percentage": total_score,
            "matched_skills": sorted(matched_skills),
            "missing_skills": sorted(missing_skills),
            "goal_match": goal_match,
            "why_this_matches": reason
        })

    matches.sort(
        key=lambda internship: internship["match_percentage"],
        reverse=True
    )

    return {
        "success": True,
        "career_goal": goal,
        "skills_provided": skills,
        "matches": matches
    }