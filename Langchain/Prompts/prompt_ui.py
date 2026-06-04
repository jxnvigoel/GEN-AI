from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

model=ChatGroq(model_name="llama-3.1-8b-instant")
st.header("AI Tool")
st.subheader("Static Prompt")
# static prompt
query=st.text_input("Enter your prompt")
if st.button("Submit"):
    st.text(model.invoke(query).content)
# for dynamic prompt
# make your own prompt and make some user input fields and pass them to the prompt
st.subheader("Dynamic Prompt")
name=st.text_input("Enter your name")
age=st.text_input("Enter your age")
if st.button("Submit2"):
    st.text(model.invoke(f"My name is {name} and I am {age} years old").content)
# we prefer using prompt template instead of f-strings
from langchain_core.prompts import PromptTemplate,load_prompt
# prompt=PromptTemplate(input_variables=["name","age"],template="My name is {name} and I am {age} years old")
prompt=load_prompt("prompt.json")
# if st.button("Submit3"):
#     st.text(model.invoke(prompt.format(name=name,age=age)).content)

# usimg CHAINS
# chain can only be used when we have a prompt template , we cant use it with f-string..
if st.button("Submit3"):
    chain=prompt|model
    st.text(chain.invoke({"name":name,"age":age}).content)