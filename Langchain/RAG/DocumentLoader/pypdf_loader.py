from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('week10-11.pdf')
docs=loader.load()
print(len(docs))
print(docs[0])
