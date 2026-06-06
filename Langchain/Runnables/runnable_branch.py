from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableBranch ,RunnableLambda, RunnableParallel, RunnablePassthrough
load_dotenv()

prompt=PromptTemplate(
    template='generate a  joke on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='generate a short summary on {topic}',
    input_variables=['topic']
)
llm=HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()

initial_chain=RunnableSequence(prompt,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>500,prompt2|model|parser),
    (lambda x:len(x.split())<500,RunnablePassthrough()),
    RunnablePassthrough()
)

final=RunnableSequence(initial_chain,branch_chain)
print(final.invoke({'topic':'ai'}))