from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(repo_id='meta-llama/Meta-Llama-3-8B-Instruct')
model=ChatHuggingFace(llm=llm)
prompt=PromptTemplate(
    template='give a name to following poem  \n {poem}',
    input_variables=['poem']
)
parser=StrOutputParser()
chain=prompt|model|parser
loader=TextLoader('poem.txt')

docs=loader.load()
# print(docs)
# print(type(docs[0]))
# print(type(docs))
data=docs[0].page_content
print(chain.invoke({'poem':data}))