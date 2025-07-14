import os
import sys
import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app
from dotenv import load_dotenv
os.environ["ADK_APP_MODULE"] = "agent"

# Path to the directory containing your agent code (e.g., where agent.py lives)
AGENTS_DIR = os.path.dirname(os.path.abspath(__file__))

# Use a SQLite file for session history
SESSION_DB_URL = "sqlite:///./sessions.db"

# Control which origins can access your API (CORS)
ALLOWED_ORIGINS = ["http://localhost", "http://localhost:3000", "*"]

# Enable the ADK debugging UI
ENABLE_WEB = True

app: FastAPI = get_fast_api_app(
    agents_dir=AGENTS_DIR,
    session_service_uri=SESSION_DB_URL,
    allow_origins=ALLOWED_ORIGINS,
    web=ENABLE_WEB,
)
# Add custom endpoints
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
@app.get("/agent-info")
async def agent_info():
    """Provide agent information"""
    from multi_tool_agent import root_agent
    return {
        "agent_name": root_agent.name,
        "description": root_agent.description,
        "model": root_agent.model,
        "tools": [t.__name__ for t in root_agent.tools]
    }
if __name__ == "__main__":
    print("Starting FastAPI server...")
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=9999, 
        reload=False
    )