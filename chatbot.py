from flask import Flask, request, jsonify, send_file
import difflib

app = Flask(__name__)

# Simple FAQ dataset (you can expand this)
faqs = {
    "what is python": "Python is a popular programming language known for its simplicity and versatility.",
    "what is flask": "Flask is a lightweight Python web framework used to build web applications.",
    "how to install python": "You can install Python from the official website python.org or using package managers.",
    "what is github": "GitHub is a platform for hosting and collaborating on code using Git version control."
}

@app.route('/')
def home():
    # Serve the frontend.html file
    return send_file("chatbot.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "").lower()

    # Find closest matching FAQ
    closest_match = difflib.get_close_matches(question, faqs.keys(), n=1, cutoff=0.5)

    if closest_match:
        answer = faqs[closest_match[0]]
    else:
        answer = "Sorry, I don't have an answer for that yet."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
