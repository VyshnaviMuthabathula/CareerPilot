# CareerPilot - AI Career Agent



CareerPilot is an AI-powered career assistant designed to help students discover suitable internship opportunities, understand their skill gaps, prepare application materials, practice interview questions, and track internship applications.



## Features



- Career goal analysis

- Resume skill analysis

- Internship matching

- Match percentage and skill-gap analysis

- Application material generation

- Interview question generation

- Application tracking

- Persistent SQLite database storage

- End-to-end career workflow



## CareerPilot Workflow



Career Goal

    |

    v

Resume Analysis

    |

    v

Skill Detection

    |

    v

Internship Matching

    |

    v

Recommended Role

    |

    v

Application Materials

    |

    v

Interview Preparation

    |

    v

Application Tracking



## Technology Stack



- Python

- FastAPI

- Pydantic

- SQLite

- Uvicorn

- REST API

- Swagger UI



## How to Run



1. Activate the virtual environment:



.\venv\Scripts\Activate.ps1



2. Start the FastAPI server:



python -m uvicorn app.main:app --reload



3. Open Swagger UI:



http://127.0.0.1:8000/docs



## Main API Endpoints



GET / - Check API status



GET /health - Health check



POST /career/analyze - Analyze career goal



POST /resume/analyze - Analyze resume skills



POST /internships/match - Match internships



POST /application/generate - Generate application materials



POST /interview/generate - Generate interview questions



POST /applications/add - Add an application



GET /applications - View applications



PUT /applications/{application\_id} - Update application status



POST /careerpilot/run - Run complete career workflow



## Example



Career Goal:



Python AI internship



Skills:



Python, Machine Learning, Artificial Intelligence, JavaScript, SQL, Git



Recommended Role:



AI/ML Intern



Match:



100%



## Application Tracking



CareerPilot uses SQLite to persist internship applications.



Supported statuses:



- Saved

- Applied

- Interview

- Selected

- Rejected



Applications remain available after restarting the FastAPI server.



## Project Status



Core backend: Completed



CareerPilot currently provides a working end-to-end backend workflow for career analysis, internship matching, application preparation, interview preparation, and application tracking.



## Future Improvements



- Real AI/LLM integration

- Resume PDF upload and parsing

- Live internship/job search

- Personalized skill-gap recommendations

- Interview answer evaluation

- Web-based frontend

- User authentication

- Application reminders and notifications


