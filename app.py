
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

responses = {
    "hello": "Hello! Welcome to the Student Helpdesk Chatbot.",
    "course": "We provide information about CSE, AIML, IT, and other departments.",
    "schedule": "Classes usually start from 9:00 AM and continue till 4:00 PM.",
    "fees": "Please contact the administration office for detailed fee structure.",
    "exam": "Exam schedules are updated on the college portal.",
    "bye": "Thank you for using the Student Helpdesk Chatbot."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()

    for key in responses:
        if key in user_message:
            return jsonify({"response": responses[key]})

    return jsonify({
        "response": "Sorry, I could not understand your query. Please try again."
    })

if __name__ == "__main__":
    app.run(debug=True)
