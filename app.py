from flask import Flask, render_template
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

ai_template = """
Answer the question below.
There is the conversation history : {context}
Question: {question}
Answer:
"""

model = OllamaLLM(model="moondream")
prompt = ChatPromptTemplate.from_template(ai_template)
chain = prompt | model

result = chain.invoke({"context": "", "question": "Hi!"})
print("Bot:  ",result)
