from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from aitemplate import template as ai_template


model = OllamaLLM(model="llama3")

model.invoke(input="")
prompt = ChatPromptTemplate.from_template(ai_template)
chain = prompt | model

def conersation_hander():
    context = ""
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": " ", "question": " "})
        print("Bot: ", result)
         
if __name__=="__main__":
    conersation_hander()