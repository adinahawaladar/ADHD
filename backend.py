# backend.py
import gradio as gr
import google.generativeai as genai
import random
import json
from datetime import datetime, timedelta
from dataset import get_questions

# Set up Gemini API
GEMINI_API_KEY = "AIzaSyC18T8mPJUjxUPqQRlFXqCgMiHIXKGxrNo"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")

# Global storage
user_responses = []  # Store ADHD questionnaire answers
user_info = {"name": "", "age": "", "gender": ""}
user_progress = {"completed": 0, "total": 200}

def process_user_info(user_input):
    """Simulate user profile processing."""
    return f"User information processed: {user_input}"

def store_user_info(response):
    """Stores user responses to ADHD questions."""
    user_responses.append(response)
    return "Response recorded!"

def generate_response(message):
    """Generate chatbot response using Gemini AI."""
    try:
        prompt = f"User said: '{message}'. Provide a helpful ADHD-related response."
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def generate_progress_report(user_details):
    """Generates a progress report including user details and suggestions."""
    if not user_responses:
        return "Please complete the ADHD questionnaire first."
    
    # Calculate risk score
    risk_score = sum(1 for ans in user_responses if ans in ["Often", "Sometimes"])
    risk_level = "Low" if risk_score < 5 else "Moderate" if risk_score < 8 else "High"
    recovery_date = (datetime.now() + timedelta(days=risk_score * 2)).strftime("%Y-%m-%d")
    
    # Personalized suggestions
    suggestions = {
        "Low": "Maintain good habits. Consider regular breaks and mindfulness exercises.",
        "Moderate": "You might benefit from structured routines and focus techniques.",
        "High": "Consult a specialist and try guided ADHD strategies to improve focus."
    }
    
    report = f"""ADHD Progress Report
    
    Risk Level: {risk_level}
    Estimated Improvement Date: {recovery_date}
    
    Suggested Actions: {suggestions[risk_level]}"""

    return report
def store_user_response(user_input):
    """Validates and stores user responses for the ADHD questionnaire."""
    valid_options = ["Never", "Sometimes", "Often", "Always"]
    if user_input not in valid_options:
        return f"Invalid choice: {user_input}. Please choose from {valid_options}."

    user_responses.append(user_input)
    return "Response saved!"


def ask_adhd_question():
    """Fetches the next ADHD-related question from the dataset."""
    questions = get_questions()  # Get questions from dataset
    print("DEBUG: Questions List:", questions)  # Check if questions exist

    if user_progress["completed"] < user_progress["total"]:
        question = questions[user_progress["completed"]]
        user_progress["completed"] += 1
        print("DEBUG: Question:", question)  # Debug question format
        return {
            "question": question.get("question", "No question found"),
            "options": question.get("options", [])  # Ensure options exist
        }
    
    return {"question": "All questions completed.", "options": []}


def update_progress():
    """Updates user's progress."""
    if user_progress["completed"] < user_progress["total"]:
        user_progress["completed"] += 1
    return generate_progress_report(user_info)
