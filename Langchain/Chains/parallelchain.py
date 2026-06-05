from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1=ChatGroq(model_name='llama-3.1-8b-instant')
llm=HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model2=ChatHuggingFace(llm=llm)

prompt=PromptTemplate(
    template='give me crisp and short notes of the {text}',
    input_variables=['text']
)
prompt2=PromptTemplate(
    template='give me 5 short one word question answer from the {text}',
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='merge the notes and quiz into a single document /n {notes},{quiz}',
    input_variables=['notes','quiz']
)

parser=StrOutputParser()

parralel_chain=RunnableParallel(
    {
        'notes':prompt|model1|parser,
        'quiz':prompt2|model2|parser
    }
)
merge_chain=prompt3|model1|parser
final_chain=parralel_chain|merge_chain
print(final_chain.invoke({'text':'AI is a branch of computer science that is concerned with the development of intelligent machines that can perform tasks that typically require human intelligence. AI is a rapidly growing field that is having a significant impact on our lives. AI is used in a wide range of applications, including healthcare, finance, and transportation. AI is also used in a wide range of products, including smartphones, cars, and robots. AI is a powerful tool that has the potential to change our lives for the better. AI is a rapidly growing field that is having a significant impact on our lives. AI is used in a wide range of applications, including healthcare, finance, and transportation. AI is also used in a wide range of products, including smartphones, cars, and robots. AI is a powerful tool that has the potential to change our lives for the better.'}))
final_chain.get_graph().print_ascii()