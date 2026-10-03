# AI Software Engineer Agent

A production-style starter for an AI software engineering agent. It turns a plain-English software request into requirements, architecture, implementation tasks, tests, security checks, and an exportable project plan.

## Features
- AI-agent workflow UI
- Requirement analysis
- Architecture planning
- Implementation task generation
- Test and security review stages
- Project memory model
- FastAPI backend
- Vercel-ready frontend
- GitHub Actions CI
- Environment-variable based AI integration

## Run locally

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
Open `frontend/index.html` with a static server, or deploy the frontend to Vercel.

Set `API_BASE_URL` in frontend/app.js if the backend is hosted separately.

## Important
The repository uses a deterministic demo agent when no LLM key is configured. This makes the portfolio project immediately runnable while keeping the architecture ready for a real model provider.
