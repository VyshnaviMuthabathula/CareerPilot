from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.agents.career_agent import analyze_career_goal
from app.agents.resume_analyzer import analyze_resume
from app.agents.internship_matcher import match_internships
from app.agents.application_generator import generate_application_materials
from app.agents.interview_generator import generate_interview_questions
from app.services.application_tracker import (
    add_application,
    get_applications,
    update_application_status
)
from app.agents.career_workflow import run_career_workflow

app = FastAPI(
    title="CareerPilot",
    description="AI Career Agent for students",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://careerpilot-sz2z.onrender.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CareerGoalRequest(BaseModel):
    goal: str


@app.get("/")
def home():
    return {
        "message": "CareerPilot API is running!",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/career/analyze")
def analyze_career(request: CareerGoalRequest):
    return analyze_career_goal(request.goal)
class ResumeRequest(BaseModel):
    resume_text: str


@app.post("/resume/analyze")
def analyze_resume_endpoint(request: ResumeRequest):
    return analyze_resume(request.resume_text)
class InternshipMatchRequest(BaseModel):
    goal: str
    skills: list[str]


@app.post("/internships/match")
def match_internships_endpoint(request: InternshipMatchRequest):
    return match_internships(request.goal, request.skills)
class ApplicationMaterialRequest(BaseModel):
    goal: str
    skills: list[str]
    target_role: str


@app.post("/application/generate")
def generate_application_endpoint(request: ApplicationMaterialRequest):
    return generate_application_materials(
        request.goal,
        request.skills,
        request.target_role
    )
class InterviewRequest(BaseModel):
    target_role: str
    skills: list[str]


@app.post("/interview/generate")
def generate_interview_endpoint(request: InterviewRequest):
    return generate_interview_questions(
        request.target_role,
        request.skills
    )
class ApplicationRequest(BaseModel):
    role: str
    company: str
    status: str = "Saved"


@app.post("/applications/add")
def add_application_endpoint(request: ApplicationRequest):
    return add_application(
        request.role,
        request.company,
        request.status
    )


@app.get("/applications")
def get_applications_endpoint():
    return get_applications()


class ApplicationStatusRequest(BaseModel):
    status: str


@app.put("/applications/{application_id}")
def update_application_endpoint(
    application_id: int,
    request: ApplicationStatusRequest
):
    return update_application_status(
        application_id,
        request.status
    )
class CareerWorkflowRequest(BaseModel):
    goal: str
    resume_text: str


@app.post("/careerpilot/run")
def run_careerpilot_endpoint(request: CareerWorkflowRequest):
    return run_career_workflow(
        request.goal,
        request.resume_text
    )