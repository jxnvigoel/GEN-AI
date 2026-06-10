from langchain_community.document_loaders import WebBaseLoader

url='https://www.flipkart.com/apple-macbook-air-m4-16-gb-1-tb-ssd-macos-sequoia-mdg54hn-a/p/itm50e339cd5bef4?pid=COMHMHMJZNF9MUQD&marketplace=FLIPKART&lid=LSTCOMHMHMJZNF9MUQDHO3NHT&pageUID=1781026610501'
loader=WebBaseLoader(url)
docs=loader.load()
print(len(docs))
print(docs[0].page_content)