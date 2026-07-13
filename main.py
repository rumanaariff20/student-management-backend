from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from controllers.student_controller import router

app = FastAPI(title="Student Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health Check
@app.get("/api/healthz")
def health():
    return {"status": "ok"}

# Student API
app.include_router(router)

# Home
@app.get("/")
def home():
    return {
        "message": "Student Management API Running"
    }