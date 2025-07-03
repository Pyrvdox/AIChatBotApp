from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

ai_template = """
Answer the question below.
There is the conversation history : {context}
Question: {question}
Answer:
"""

model = OllamaLLM(model="phi3")
prompt = ChatPromptTemplate.from_template(ai_template)
chain = prompt | model


def conversation_handler(convseration_context, user_question):
    result = chain.invoke({"context": convseration_context, "question": user_question})
    return result