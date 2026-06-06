from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt=PromptTemplate(
    template='generate a short 1 line joke on {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='explain the {topic}',
    input_variables=['topic']
)

llm=HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model=ChatHuggingFace(llm=llm)

parser=StrOutputParser()
passthrough=RunnablePassthrough()

joke_chain=RunnableSequence(prompt,model,parser)

parralel_chain=RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_chain,parralel_chain)
print(final_chain.invoke({'topic':'monkey'}))