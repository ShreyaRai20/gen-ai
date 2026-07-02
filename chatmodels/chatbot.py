from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

messages = [
    SystemMessage(content="you are a serious ai")
]
print("----------- welcome please enter 0 to quit -----------")

while True:
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if(prompt == '0'):
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("response: " + response.content)

print(messages)