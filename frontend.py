from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import webbrowser
import gradio as gr
import threading

from backend import (
    process_user_info,
    generate_response,
    generate_progress_report,
    ask_adhd_question,
    store_user_info
)

app = FastAPI()

# Serve static files (HTML, CSS, JS)
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Use lifespan event handlers instead of on_event
@app.on_event("startup")
async def startup():
    webbrowser.open("http://127.0.0.1:7864/foucscheck.html")





# Function to start FastAPI server in a separate thread
def start_fastapi():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)  # Change port to 8003



# Gradio Chatbot & ADHD Test UI
question_count = 0
max_questions = 6
user_details = {"name": "", "age": "", "gender": ""}

def generate_chat_response(message, chat_history):
    try:
        bot_message = generate_response(message)
        chat_history.append({"role": "user", "content": message})  # User message
        chat_history.append({"role": "assistant", "content": bot_message})  # Bot response

        return "", chat_history
    except Exception as e:
        return f"Error: {str(e)}", chat_history

def fetch_adhd_question():
    question_data = ask_adhd_question()
    if isinstance(question_data, dict):
        return question_data['question'], gr.update(choices=question_data['options'])
    return "No more questions available.", gr.update(choices=[])

def submit_answer(response):
    global question_count
    question_count += 1
    store_user_info(response)

    if question_count >= max_questions:
        return generate_progress_report(user_details), "", gr.update(choices=[])

    next_question, next_options = fetch_adhd_question()
    return "", next_question, next_options

def skip_question():
    global question_count
    question_count += 1

    if question_count >= max_questions:
        return generate_progress_report(user_details), "", gr.update(choices=[])

    next_question, next_options = fetch_adhd_question()
    return "", next_question, next_options

def set_user_details(name, age, gender):
    global user_details
    user_details = {"name": name, "age": age, "gender": gender}
    return f"User information saved: {name}, {age}, {gender}"

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# ADHD Focus Helper")

    with gr.Row():
        name_input = gr.Textbox(label="Name", placeholder="Enter your name")
        age_input = gr.Textbox(label="Age", placeholder="Enter your age")
        gender_input = gr.Radio(["Male", "Female", "Other"], label="Gender")

    save_user_button = gr.Button("Save Information")

    chatbot_interface = gr.Chatbot(label="Chat", type='messages')

    message_input = gr.Textbox(label="Your Message", placeholder="Type your message here...")
    send_button = gr.Button("Send")

    progress_report = gr.Textbox(label="Progress Report", interactive=False)
    generate_report_button = gr.Button("Generate Progress Report")

    adhd_question = gr.Textbox(label="ADHD Check-In", interactive=False)
    options = gr.Radio([], label="Your Response")
    submit_button = gr.Button("Submit Answer")
    skip_button = gr.Button("Skip Question")

    gr.HTML("<div style='text-align:center; margin-top:20px;'>"
            "<a href='http://localhost:8000/foucscheck.html' style='text-decoration:none;'>"
            "<button style='padding:10px 20px; font-size:16px; background-color:#6A5ACD; color:white; "
            "border:none; border-radius:5px; cursor:pointer;'>Back to Home</button></a></div>")

    save_user_button.click(set_user_details, inputs=[name_input, age_input, gender_input], outputs=[adhd_question])
    send_button.click(generate_chat_response, inputs=[message_input, chatbot_interface], outputs=[message_input, chatbot_interface])
    submit_button.click(submit_answer, inputs=[options], outputs=[progress_report, adhd_question, options])
    skip_button.click(skip_question, inputs=[], outputs=[progress_report, adhd_question, options])
    generate_report_button.click(lambda: generate_progress_report(user_details), inputs=[], outputs=progress_report)

# Function to start Gradio UI in a separate thread
def start_gradio():
    demo.launch()

# Run FastAPI and Gradio in parallel
if __name__ == "__main__":
    threading.Thread(target=start_fastapi, daemon=True).start()  # Start FastAPI in a thread
    start_gradio()  # Start Gradio UI
