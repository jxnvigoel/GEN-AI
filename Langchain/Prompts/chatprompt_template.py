from langchain_core.prompts import ChatPromptTemplate
# it doesnt use messages class it has its own way of representing messages
# it uses tuples to represent messages
# format is (role,message)
chat_template=ChatPromptTemplate([
('system','you are a helpful {domain} expert'),
('human','explain in simple terms what is {topic}')
])

prompt=chat_template.invoke({'domain':'cricket','topic':'dusra'})
print(prompt)