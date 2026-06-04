from langchain_core.prompts import PromptTemplate
# here we can store the template for reusing in mutiple files
prompt=PromptTemplate(input_variables=["name","age"],template="My name is {name} and I am {age} years old")
prompt.save("prompt.json")