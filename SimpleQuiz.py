# Web Quiz Backend by Jeet Panchal
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CRITICAL: This allows your HTML page to safely talk to your Python backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Your original data structure (Slightly cleaned up for web extraction)
quiz_data = {
    "Geography": [
        ["What is the capital of France?", "Paris", "Delhi", "Lagos", "Rome", 1],
        ["Which is the largest ocean?", "Atlantic", "Indian", "Pacific", "Arctic", 3],
        ["Which country has the largest population?", "India", "USA", "China", "Russia", 1]
    ],
    "Math": [
        ["2 + 2 = ?", "3", "4", "5", "6", 2],
        ["What is 10 * 5?", "40", "50", "60", "70", 2],
        ["What is the square root of 64?", "6", "7", "8", "9", 3]
    ],
    "Compsci": [
        ["Which language is for web development?", "Python", "C++", "HTML", "Java", 3],
        ["What does 'CPU' stand for?", "Central Process Unit", "Control Processing Unit", "Central Processing Unit", "Computer Personal Unit", 3],
        ["Which of these is an Operating System?", "Python", "Windows", "HTML", "Java", 2]
    ]
}

# This defines the data structure for checking answers via web requests
class AnswerSubmission(BaseModel):
    category: str
    question_index: int
    selected_option_number: int

# 2. ENDPOINT 1: Send the selected category's questions to the browser (hiding correct indices!)
@app.get("/api/questions/{category}")
def get_questions_by_category(category: str):
    category_formatted = category.strip().capitalize()
    
    if category_formatted not in quiz_data:
        return {"error": "Category not found"}
    
    questions = quiz_data[category_formatted]
    
    # Format the questions safely so the frontend can't see the answers in the source code
    safe_questions = []
    for index, q in enumerate(questions):
        safe_questions.append({
            "index": index,
            "question_text": q[0],
            "options": [q[1], q[2], q[3], q[4]]
        })
        
    return safe_questions

# 3. ENDPOINT 2: Receive the user's web click and check if they got it right
@app.post("/api/check")
def check_answer(submission: AnswerSubmission):
    category = submission.category.strip().capitalize()
    
    if category not in quiz_data:
        return {"error": "Category not found"}
        
    # Look up the actual question using the index sent by the frontend
    actual_question = quiz_data[category][submission.question_index]
    correct_option_index = actual_question[5] # The index integer (1-4)
    
    is_correct = (submission.selected_option_number == correct_option_index)
    correct_text = actual_question[correct_option_index]
    
    return {
        "correct": is_correct,
        "correct_answer_text": correct_text
    }