from flask import Flask, request, jsonify, render_template
import spacy
import difflib
from transformers import pipeline

app = Flask(__name__)

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# FAQ dictionary (expand as needed)
faqs = {
    "python": "Python is a popular programming language known for its simplicity and versatility.",
    "flask": "Flask is a lightweight Python web framework used to build web applications.",
    "github": "GitHub is a platform for hosting and collaborating on code using Git version control.",
    "ai": "Artificial Intelligence refers to systems that can perform tasks that normally require human intelligence."
}

# Load a text generation model (GPT-2 for fallback)
generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def home():
    return render_template("chatbot.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "").lower()

    # Process with NLP
    doc = nlp(question)
    keywords = [token.lemma_ for token in doc if not token.is_stop]

    # Try FAQ match using keywords
    closest_match = difflib.get_close_matches(" ".join(keywords), faqs.keys(), n=1, cutoff=0.6)
    if closest_match:
        answer = faqs[closest_match[0]]
    else:
        # Fall back to GPT-2 text generation
        try:
            result = generator(question, max_length=60, num_return_sequences=1)
            answer = result[0]["generated_text"]
        except Exception:
            answer = "Sorry, I couldn't process that question."

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
