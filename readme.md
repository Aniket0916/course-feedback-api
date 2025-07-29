# 📘 Course Feedback Web App (FastAPI + HTML UI)

A simple, beginner-friendly full-stack application using **FastAPI** and **HTML/Tailwind CSS** that allows users to submit course feedback through a clean web form.

This project is ideal for learning FastAPI basics, form handling, and creating client-facing interfaces — and is a great fit for freelance portfolio use.

---

## 🚀 Features

- Submit course feedback (name, rating, comment, category)
- Live timestamp on submission
- Input validation using Pydantic
- Clean, mobile-friendly UI using Tailwind CSS
- In-memory data storage (for learning/demo purposes)
- Fully interactive form with success/error messages

---

## 🧰 Tech Stack

- **Backend:** FastAPI, Python, Pydantic
- **Frontend:** HTML, Tailwind CSS, Jinja2 Templates
- **Server:** Uvicorn (for local development)

---

## 🖼️ Screenshot

look for websiteui.png in the folder

---

## ▶️ How to Run

### 1. Clone this repository:
bash
git clone https://github.com/Aniket0916/course-feedback-api.git
cd course-feedback-api

### 2. Install the required packages:
bash
Copy
Edit
pip install -r requirements.txt

### 3. Run the server:
bash
Copy
Edit
uvicorn main:app --reload

### 4. Visit the app in your browser:
bash
Copy
Edit
http://127.0.0.1:8000/docs


### Folder Structure
course-feedback-api/
├── main.py               # FastAPI application
├── templates/
│   └── index.html        # Feedback form (UI)
├── static/
│   └── style.css         # Optional custom styles
├── requirements.txt
└── README.md

### Future Improvements
Add SQLite or MongoDB database. As I'm just using a dictionary that is machine memory in order to store the data. We can convert the project to use SQL database to store the data. But for now I'm going to keep it as it is as i just wanted to get my hands on FastAPI and HTML
Add authentication for admin access
Store and display feedback in a table view
Export feedback as CSV or Excel
Deploy using Render, Railway, or Vercel

# License
This project is open-source and free to use for learning or portfolio purposes.
