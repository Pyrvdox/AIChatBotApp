from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from aitemplate import template as ai_template


model = OllamaLLM(model="llama3")

model.invoke(input="")
prompt = ChatPromptTemplate.from_template(ai_template)