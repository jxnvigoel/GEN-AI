from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader=DirectoryLoader(
    path='books',
    glob='*.pdf', #type of files to load
    loader_cls=PyPDFLoader
)
docs=loader.load()
# print(len(docs))
for document in docs:
    print(document.metadata)

# lazy_load
docs1=loader.lazy_load()
for document in docs1:
    print(document.metadata)
