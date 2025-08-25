from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', max_completion_tokens=50)

messages = [
    SystemMessage(
        "You are a helpful assistant. You are given a question and you need to answer it"),
    HumanMessage("where is Lahore located?"),
]


result = model.invoke(messages)

print(result.content)
