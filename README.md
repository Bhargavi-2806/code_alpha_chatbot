# code_alpha_chatbot
A simple chatbot using ai

##1. Project Overview

This project is a web‑based AI chatbot built using Python, Flask, and Natural Language Processing (NLP).
It combines:
A FAQ dictionary for accurate answers to common questions.
spaCy NLP for keyword extraction and intent detection.
A local Hugging Face GPT‑2 model for fallback text generation.
The goal was to create a mid‑level accurate chatbot without relying on paid APIs.

##2. Tools & Libraries Used

Flask → Web framework to serve chatbot backend and frontend.
spaCy → NLP library for tokenization, lemmatization, and keyword extraction.
difflib → Used for fuzzy matching between user queries and FAQ entries.
Transformers (Hugging Face) → Provides GPT‑2 text generation pipeline for fallback answers.
Torch → Backend library required by Hugging Face models.

##3. Backend Code (chatbot.py)

Key components:
Imports: Flask, spaCy, difflib, transformers.
FAQ Dictionary: Stores reliable answers for known queries.
NLP Processing: Extracts keywords and normalizes user input.
Fallback Model: GPT‑2 generates responses when FAQ doesn’t match.
Routes:
/ → Serves chatbot.html frontend.
/chat → Handles POST requests, processes questions, returns answers.

##4. Frontend (chatbot.html)

Simple HTML interface with:
Input box → User types question.
Send button → Sends query to backend.
Chat window → Displays conversation (user + bot messages).

##5. Folder Structure
Code
code_alpha_chatbot/
│
├── chatbot.py
├── requirements.txt
├── README.md
└── templates/
    └── chatbot.html
    
##6. Requirements (requirements.txt)
txt
flask
spacy
transformers
torch

##7. Command Prompt Usage

Here’s what was done in Command Prompt during development:

Install dependencies

bash
pip install flask spacy transformers torch
Download spaCy model

bash
python -m spacy download en_core_web_sm
Run the chatbot

bash
python chatbot.py
Access in browser

Code
http://127.0.0.1:5000/


##8. Challenges Faced

Pipeline errors: "question-answering" pipeline not supported in newer transformers → switched to "text-generation".
TemplateNotFound: Fixed by placing chatbot.html inside templates/ folder.
Import errors: Resolved by installing spaCy and downloading its language model.
Random answers: Improved accuracy by combining FAQ dictionary with NLP keyword matching.

## 9. What’s Useful in This Project

Hybrid approach → balances accuracy (FAQ) and flexibility (GPT‑2).
NLP integration → makes chatbot smarter by understanding user intent.
Local execution → no API costs, works offline after model download.
Expandable design → FAQ dictionary can be extended easily, NLP can be trained further.
##10. Future Improvements

Train a custom intent classifier (greetings, programming, general knowledge).
Add a JSON/CSV FAQ loader so new questions can be added without editing code.
Improve frontend with CSS and JavaScript for a modern chat UI.
Optionally connect to APIs later for advanced accuracy.
