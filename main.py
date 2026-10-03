from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict

app = FastAPI(title="AI Software Engineer Agent API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentRequest(BaseModel):
    prompt: str = Field(min_length=5, max_length=5000)
    stack: str = "auto"

class Task(BaseModel):
    id: str
    title: str
    detail: str
    status: str = "planned"

def build_plan(prompt: str, stack: str) -> Dict:
    lower = prompt.lower()
    frontend = "Next.js + TypeScript"
    backend = "FastAPI"
    database = "PostgreSQL"

    if "go" in lower or stack.lower() == "go":
        backend = "Go + REST API"
    if "shopify" in lower:
        database = "PostgreSQL + Shopify Admin API"

    return {
        "project": "AI-generated software project",
        "summary": prompt.strip(),
        "stack": {"frontend": frontend, "backend": backend, "database": database},
        "requirements": [
            "Define user roles and core user journeys",
            "Create responsive and accessible UI",
            "Implement authenticated API boundaries",
            "Persist project data and agent memory",
            "Add automated tests and error handling",
        ],
        "architecture": [
            "Frontend dashboard",
            "Agent orchestration layer",
            "Tool/API layer",
            "Persistent project memory",
            "Test and security pipeline",
        ],
        "tasks": [
            Task(id="T-01", title="Requirements", detail="Convert the request into explicit functional and non-functional requirements."),
            Task(id="T-02", title="Architecture", detail=f"Design a maintainable system using {frontend}, {backend}, and {database}."),
            Task(id="T-03", title="Implementation", detail="Generate modules, API contracts, validation and error handling."),
            Task(id="T-04", title="Testing", detail="Create unit, integration and API test cases."),
            Task(id="T-05", title="Security review", detail="Check authentication boundaries, secrets, input validation and common API risks."),
            Task(id="T-06", title="Deployment", detail="Prepare environment variables, CI and deployment configuration."),
        ],
        "memory": {
            "project_goal": prompt.strip(),
            "decisions": [f"Preferred stack: {stack}"],
            "facts": ["Agent memory is represented as structured project context."]
        },
        "created_at": datetime.utcnow().isoformat() + "Z"
    }

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-software-engineer-agent"}

@app.post("/agent/plan")
def create_plan(req: AgentRequest):
    return build_plan(req.prompt, req.stack)

@app.post("/agent/review")
def review(req: AgentRequest):
    return {
        "summary": "Static portfolio review completed.",
        "checks": [
            {"name": "Input validation", "status": "PASS"},
            {"name": "API boundary", "status": "PASS"},
            {"name": "Secret handling", "status": "CHECK"},
            {"name": "Automated tests", "status": "RECOMMENDED"},
        ],
        "notes": [
            "Use environment variables for provider keys.",
            "Add authentication before exposing project generation publicly.",
            "Run dependency and security scanning in CI."
        ]
    }
