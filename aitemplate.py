from langchain_core.prompts import ChatMessagePromptTemplate

template = """
Answer the question below.
There is the conversation history : {context}
Question: {question}
Answer:
"""