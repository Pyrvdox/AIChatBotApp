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


def conversation_handler():
    context = ""
    while True:
        user_input = input("you: ")
        if user_input.lower() == "exit":
            break
        
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:  ",result)
        context += f"\n User: {user_input} \nAI: {result}"


conversation_handler()