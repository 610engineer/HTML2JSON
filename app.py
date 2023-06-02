
# -*- coding: utf-8 -*-
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from elasticsearch_func import add_document
from langchain.document_loaders import UnstructuredHTMLLoader, DirectoryLoader

import os
import env

def main():


    # test
    """
    loader = UnstructuredHTMLLoader("C:\\Users\\masat\\OneDrive\\デスクトップ\\Workspace\\MQDヘルプ\\HTMLのみ\\64bitOSで利用する場合.html", encoding= "shift-jis")
    print(loader)
    documents = loader.load()
    print(documents)

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()

    db = ElasticVectorSearch.from_documents(docs, embeddings, 
                                            elasticsearch_url=os.environ.get('ELASTICSEARCH_URL'),
                                            index_name="document_test")
    print(db)
    """

    # test
    loader = DirectoryLoader("C:\\Users\\masat\\OneDrive\\デスクトップ\\Workspace\\MQDhelp\\HTML", glob="**/*.html", )
    print(loader)
    documents = loader.load()
    print(documents)

    embedding = OpenAIEmbeddings()
    """
    elastic_vector_search = ElasticVectorSearch(
        elasticsearch_url="http://localhost:9200",
        index_name="document_test",
        embedding=embedding
    )

    query = "「データベースエンジン」を含む文章"
    answer = elastic_vector_search.similarity_search(query)

    print("ANSWER", answer[0].page_content)
    """




if __name__ == "__main__":
    main()