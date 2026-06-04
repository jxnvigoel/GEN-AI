from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
model=ChatGroq(model_name='llama-3.1-8b-instant')
messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
    ]
response=model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)
# there are 3 types of mesaages only in langchain
# they are used so that llm knows which mesage is from whom in chat history
