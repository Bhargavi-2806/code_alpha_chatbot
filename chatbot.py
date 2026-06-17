from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load a pre-trained Question Answering pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# A context paragraph for the model to answer from
# You can expand this with more text about topics you want your bot to handle
context = """
Python is a programming language widely used for web development, data science, and automation.
Flask is a lightweight Python web framework used to build web applications.
GitHub is a platform for hosting and collaborating on code using Git version control.
Artificial Intelligence (AI) refers to systems that can perform tasks that normally require human intelligence.
"""

@app.route('/')
def home():
    return render_template("frontend.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    try:
        # Use the QA pipeline to find an answer
        result = qa_pipeline(question=question, context=context)
        answer = result["answer"]
    except Exception as e:
        answer = "Sorry, I couldn't process that question."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
