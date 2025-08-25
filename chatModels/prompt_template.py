from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', max_completion_tokens=50)

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke(
    {"language": "Italian", "text": "how are you?"})

# print(prompt.to_messages())

response = model.invoke(prompt)
print(response.content)
