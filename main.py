from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

# Static and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# In-memory DB
course_feedbacks = {}

class Feedback(BaseModel):
    feedback_id: int
    course_name: str
    student_name: str
    rating: float
    comment: Optional[str] = None
    category: Optional[str] = "General"
    submitted_at: Optional[str] = datetime.now().isoformat()

@app.get("/", response_class=HTMLResponse)
def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": ""})

@app.post("/submit/", response_class=HTMLResponse)
def submit_feedback(
    request: Request,
    feedback_id: int = Form(...),
    course_name: str = Form(...),
    student_name: str = Form(...),
    rating: float = Form(...),
    comment: str = Form(""),
    category: str = Form("General")
):
    if feedback_id in course_feedbacks:
        return templates.TemplateResponse("index.html", {"request": request, "message": "❌ Feedback ID already exists."})
    
    feedback = Feedback(
        feedback_id=feedback_id,
        course_name=course_name,
        student_name=student_name,
        rating=rating,
        comment=comment,
        category=category,
        submitted_at=datetime.now().isoformat()
    )
    course_feedbacks[feedback_id] = feedback
    return templates.TemplateResponse("index.html", {"request": request, "message": "✅ Feedback submitted!"})
