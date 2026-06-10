from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("file.pdf")
docs=loader.load()

# text='''
# sir i have a doubt , i have learnt prompting in langchain , since that is mostly used as of i have learnt . so do we need to learn prompting using this notebook too , or can i make a new notebook on prompting i learnt in langchain
# [1:55 PM]cz all the same things i could do in langchain and since i knew that i could do same things using langchain and make a similar notebook .
# '''

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

# result=splitter.split_text(text)
result=splitter.split_documents(docs)

print(result[0].page_content)