from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', max_completion_tokens=50)

system_template = "Translate the following from English into {language}"

# A PromptTemplate is like a blueprint for your AI questions.
# Instead of writing the same full prompt again and again, you create a template with placeholders.
# Then you just fill in the blanks when you want to ask the model something.
# Example:
# Template:
# Translate this text into {language}: {text}

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke(
    {"language": "Italian", "text": "how are you?"})

# print(prompt.to_messages())

response = model.invoke(prompt)
print(response.content)
