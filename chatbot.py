from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI()

chatHistory = []

while True:
    user_input = input("you: ")
    chatHistory.append(user_input)
    if user_input == 'Exit':
        break
    result = model.invoke(chatHistory)
    print('AI: ', result.content)
