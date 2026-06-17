from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load a text generation model (GPT-2)
generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def home():
    # Flask looks inside the 'templates' folder for chatbot.html
    return render_template("chatbot.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    try:
        # Generate a response using GPT-2
        result = generator(question, max_length=100, num_return_sequences=1)
        answer = result[0]["generated_text"]
    except Exception as e:
        answer = "Sorry, I couldn't process that question."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
