from flask import Flask, render_template
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
There is the conversation history : {context}
Question: {question}
Answer:
"""

model = OllamaLLM(model="moondream")

app = Flask(__name__)

conversation = []

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)