import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [goal, setGoal] = useState("");
  const [resumeText, setResumeText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [interviewAnswers, setInterviewAnswers] = useState({});
  const [practiceFeedback, setPracticeFeedback] = useState({});

  const [applications, setApplications] = useState([]);
  const [applicationRole, setApplicationRole] = useState("");
  const [applicationCompany, setApplicationCompany] = useState("");

  // Load saved applications from backend
  const loadApplications = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/applications"
      );

      const data = await response.json();

      if (data.success) {
        setApplications(data.applications);
      }
    } catch (err) {
      console.error("Could not load applications:", err);
    }
  };

  // Load applications when page opens
  useEffect(() => {
    loadApplications();
  }, []);

  // Add a new application
  const addApplication = async () => {
    if (
      !applicationRole.trim() ||
      !applicationCompany.trim()
    ) {
      setError("Please enter the role and company.");
      return;
    }

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/applications/add",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            role: applicationRole,
            company: applicationCompany,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Could not add application."
        );
      }

      setApplicationRole("");
      setApplicationCompany("");
      setError("");

      await loadApplications();
    } catch (err) {
      console.error("Could not add application:", err);
      setError("Could not add the application.");
    }
  };

  // Update application status
  const updateApplicationStatus = async (
    applicationId,
    newStatus
  ) => {
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/applications/${applicationId}`,
        {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            status: newStatus,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Could not update application."
        );
      }

      setError("");

      await loadApplications();
    } catch (err) {
      console.error(
        "Could not update application:",
        err
      );

      setError(
        "Could not update the application status."
      );
    }
  };

  // Use the recommended role in the application tracker
  const useRecommendedRole = () => {
    if (!result || !result.recommended_role) {
      return;
    }

    setApplicationRole(result.recommended_role);
    setApplicationCompany("");
    setError("");

    setTimeout(() => {
      document
        .getElementById("applications")
        ?.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
    }, 100);
  };

  // Analyze career
  const analyzeCareer = async () => {
    if (!goal.trim() || !resumeText.trim()) {
      setError(
        "Please enter your career goal and resume information."
      );
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/careerpilot/run",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            goal: goal,
            resume_text: resumeText,
          }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Something went wrong."
        );
      }

      setResult(data);
    } catch (err) {
      setError(
        "Could not connect to CareerPilot backend. Make sure the FastAPI server is running."
      );
    } finally {
      setLoading(false);
    }
  };
  function practiceAnswer(index) {

    const answer = (interviewAnswers[index] || "").trim();

    if (!answer) {
      setPracticeFeedback((previous) => ({
        ...previous,
        [index]:
          "Type your answer first, then click Practice Answer.",
      }));
      return;
    }

    setPracticeFeedback((previous) => ({
      ...previous,
      [index]:
        "Good start! Make your answer stronger by including a clear example, what you did, and what you learned.",
    }));
  }

  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <div>
          <h1>CareerPilot</h1>
          <p>AI Career Agent</p>
        </div>

        <span className="status">
          ● AI Career Assistant
        </span>
      </header>

      <main className="container">

        {/* Career Analysis Hero */}
        <section className="hero">
          <h2>
            Find Your Best Career Path 🚀
          </h2>

          <p>
            Enter your career goal and resume information.
            CareerPilot will analyze your skills, find suitable
            internship roles, and prepare you for applications
            and interviews.
          </p>
        </section>

        {/* Career Analysis Form */}
        <section className="input-card">
          <h3>Start Your Career Analysis</h3>

          <label>Career Goal</label>

          <input
            type="text"
            placeholder="Example: Python AI internship"
            value={goal}
            onChange={(e) =>
              setGoal(e.target.value)
            }
          />

          <label>Resume / Skills</label>

          <textarea
            placeholder="Enter your resume information or skills..."
            value={resumeText}
            onChange={(e) =>
              setResumeText(e.target.value)
            }
            rows="8"
          />

          <button
            onClick={analyzeCareer}
            disabled={loading}
          >
            {loading
              ? "Analyzing..."
              : "Analyze My Career"}
          </button>

          {error && (
            <p className="error">
              {error}
            </p>
          )}
        </section>

        {/* Career Results */}
        {result && (
          <section className="results">

            <h2>Your CareerPilot Results</h2>

            {/* Recommended Role */}
            <div className="result-card highlight">

              <span>Recommended Role</span>

              <h3>
                {result.recommended_role}
              </h3>

              <button
                onClick={useRecommendedRole}
                style={{
                  marginTop: "18px",
                  padding: "10px 17px",
                  border: "1px solid #6366f1",
                  borderRadius: "9px",
                  background: "#ffffff",
                  color: "#4f46e5",
                  fontWeight: "700",
                  cursor: "pointer"
                }}
              >
                Use This Role →
              </button>

            </div>

            {/* Career Goal + Skills */}
            <div className="result-grid">

              <div className="result-card">
                <h3>Career Goal</h3>

                <p>
                  {
                    result.career_goal_analysis
                      .career_goal
                  }
                </p>
              </div>

              <div className="result-card">
                <h3>Skills Detected</h3>

                <div className="skills">
                  {result.resume_analysis.skills_detected.map(
                    (skill) => (
                      <span key={skill}>
                        {skill}
                      </span>
                    )
                  )}
                </div>
              </div>

            </div>

            {/* Internship Matches */}
            <div className="result-card">

              <h3>Internship Matches</h3>

              {result.internship_matching.matches.map(
                (match) => (
                  <div
                    className="match"
                    key={match.role}
                  >
                    <div>
                      <strong>
                        {match.role}
                      </strong>

                      <p>
                        {match.company_type}
                      </p>
                    </div>

                    <span className="percentage">
                      {match.match_percentage}%
                    </span>
                  </div>
                )
              )}

            </div>

            {/* Application Preparation */}
            <div className="result-card">

              <h3>
                Application Preparation
              </h3>

              <h4>
                Tell Me About Yourself
              </h4>

              <div className="material-box">
                <p>
                  {
                    result.application_materials
                      .tell_me_about_yourself
                  }
                </p>

                <button
                  onClick={() =>
                    navigator.clipboard.writeText(
                      result.application_materials
                        .tell_me_about_yourself
                    )
                  }
                >
                  Copy
                </button>
              </div>

              <h4>
                Why Are You Interested?
              </h4>

              <p>
                {
                  result.application_materials
                    .why_interested
                }
              </p>

            </div>

            {/* Interview Preparation */}
            <div className="result-card">
              <h3>
                Interview Preparation
              </h3>

              <p className="section-description">
                Practice your answers before the interview.
              </p>

              <div className="interview-questions">
                {result.interview_preparation.general_questions.map(
                  (question, index) => (
                    <div className="interview-question" key={question}>
                      <h4>
                        {index + 1}. {question}
                      </h4>

                      <textarea
                        style={{
                          display: "block",
                          width: "100%",
                          height: "120px",
                          padding: "14px",
                          border: "2px solid #4f7cff",
                          borderRadius: "10px",
                          backgroundColor: "#ffffff",
                          color: "#263248",
                          boxSizing: "border-box",
                          fontSize: "15px",
                        }}
    
                        placeholder="Type your answer here..."
                        rows="4"
                        value={interviewAnswers[index] || ""}
                        onChange={(event) =>
                          setInterviewAnswers((previous) => ({
                            ...previous,
                            [index]: event.target.value,
                          }))
                        }
                      />
                      <button 
                        className="practice-button"
                        onClick={() =>practiceAnswer(index)}
                      >                      
                        Practice Answer
                      
                      </button>
                      {practiceFeedback[index] && (
                        <p className="practice-feedback">
                          {practiceFeedback[index]}
                        </p>
                      )}
                    </div>
                  )
                )}
              </div>
            </div>
          </section>
        )}

        {/* Application Tracker */}
        <section
          id="applications"
          className="result-card applications-section"
        >

          <h2>My Applications</h2>

          <p>
            Track your internship applications and
            their current status.
          </p>

          {/* Add Application */}
          <div className="application-form">

            <div className="form-field">
              <label>Role</label>

              <input
                type="text"
                placeholder="Example: AI/ML Intern"
                value={applicationRole}
                onChange={(e) =>
                  setApplicationRole(
                    e.target.value
                  )
                }
              />
            </div>

            <div className="form-field">
              <label>Company</label>

              <input
                type="text"
                placeholder="Example: Demo AI Company"
                value={applicationCompany}
                onChange={(e) =>
                  setApplicationCompany(
                    e.target.value
                  )
                }
              />
            </div>

            <button onClick={addApplication}>
              Save Application
            </button>

          </div>

          {error && (
            <p className="error">
              {error}
            </p>
          )}

          {/* Application List */}
          {applications.length === 0 ? (
            <p>
              No applications added yet.
            </p>
          ) : (
            <div className="applications-list">

              {applications.map(
                (application) => (
                  <div
                    className="match"
                    key={
                      application.application_id
                    }
                  >

                    <div>
                      <strong>
                        {application.role}
                      </strong>

                      <p>
                        {application.company}
                      </p>
                    </div>

                    <select
                      value={application.status}
                      onChange={(e) =>
                        updateApplicationStatus(
                          application.application_id,
                          e.target.value
                        )
                      }
                    >

                      <option value="Saved">
                        Saved
                      </option>

                      <option value="Applied">
                        Applied
                      </option>

                      <option value="Interview">
                        Interview
                      </option>

                      <option value="Selected">
                        Selected
                      </option>

                      <option value="Rejected">
                        Rejected
                      </option>

                    </select>

                  </div>
                )
              )}

            </div>
          )}

        </section>

      </main>
    </div>
  );
}

export default App;