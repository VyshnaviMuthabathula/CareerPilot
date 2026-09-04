from app.agents.career_agent import analyze_career_goal
from app.agents.resume_analyzer import analyze_resume
from app.agents.internship_matcher import match_internships
from app.agents.application_generator import generate_application_materials
from app.agents.interview_generator import generate_interview_questions


def run_career_workflow(
    goal: str,
    resume_text: str
) -> dict:
    """
    Run the complete CareerPilot workflow.
    """

    goal = goal.strip()
    resume_text = resume_text.strip()

    if not goal:
        return {
            "success": False,
            "message": "Please provide a career goal."
        }

    if not resume_text:
        return {
            "success": False,
            "message": "Please provide resume text."
        }

    # Step 1: Analyze career goal
    career_analysis = analyze_career_goal(goal)

    # Step 2: Analyze resume
    resume_analysis = analyze_resume(resume_text)

    if not resume_analysis.get("success"):
        return resume_analysis

    skills = resume_analysis["skills_detected"]

    if not skills:
        return {
            "success": False,
            "message": "No relevant skills were detected in the resume."
        }

    # Step 3: Match internships
    internship_results = match_internships(goal, skills)

    if not internship_results.get("success"):
        return internship_results

    best_match = internship_results["matches"][0]
    target_role = best_match["role"]

    # Step 4: Generate application materials
    application_materials = generate_application_materials(
        goal,
        skills,
        target_role
    )

    # Step 5: Generate interview questions
    interview_questions = generate_interview_questions(
        target_role,
        skills
    )

    return {
        "success": True,
        "career_goal_analysis": career_analysis,
        "resume_analysis": resume_analysis,
        "internship_matching": internship_results,
        "recommended_role": target_role,
        "application_materials": application_materials,
        "interview_preparation": interview_questions
    }