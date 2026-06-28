from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=0, max_completion_tokens=10)

#result = model.invoke("What is the capital of India?")

result = model.invoke("Write a 5 line poen on cricekt")

#print(result)

print(result.content)
