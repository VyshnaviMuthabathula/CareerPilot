def analyze_career_goal(goal: str) -> dict:
    """
    Analyze a student's career goal and generate
    role-specific career recommendations.
    """

    goal = goal.strip()

    if not goal:
        return {
            "success": False,
            "message": "Please provide a career goal."
        }

    goal_lower = goal.lower()

    if "python" in goal_lower or "ai" in goal_lower or "machine learning" in goal_lower:
        recommendations = [
            "Strengthen Python programming skills",
            "Build 2-3 AI or machine learning projects",
            "Learn important machine learning concepts",
            "Prepare Python and machine learning interview questions"
        ]

    elif "web" in goal_lower or "frontend" in goal_lower or "full stack" in goal_lower:
        recommendations = [
            "Strengthen HTML, CSS and JavaScript skills",
            "Build responsive web projects",
            "Learn a modern framework such as React",
            "Prepare frontend and web development interview questions"
        ]

    elif "data" in goal_lower or "analyst" in goal_lower:
        recommendations = [
            "Strengthen Python and SQL skills",
            "Practice data analysis with real datasets",
            "Learn visualization tools such as Power BI or Tableau",
            "Prepare SQL and data analysis interview questions"
        ]

    else:
        recommendations = [
            "Analyze your current skills",
            "Identify skills required for the target role",
            "Build relevant projects for your portfolio",
            "Prepare for interviews related to the target role"
        ]

    return {
        "success": True,
        "career_goal": goal,
        "next_steps": recommendations
    }