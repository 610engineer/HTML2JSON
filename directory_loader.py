import glob
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from elasticsearch_func import add_document
from langchain.document_loaders import DirectoryLoader

import os
import env


def insert_to_elasticsearch(folder_path):

    ### htmlファイルをElasticsearchに流す ###
    loader = DirectoryLoader(folder_path, glob="**/*.html")

    documents = loader.load()

    # elasticsearchに入れるために分割
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()

    print("DOCS", docs)

    # documentをelasticsearchにインサート
    db = ElasticVectorSearch.from_documents(docs, embeddings, 
                                            elasticsearch_url=os.environ.get('ELASTICSEARCH_URL'),
                                            index_name="document_test")


    ### htmファイルをElasticsearchに流す ###
    loader = DirectoryLoader(folder_path, glob="**/*.htm")

    documents = loader.load()

    # elasticsearchに入れるために分割
    text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()

    print("DOCS", docs)

    # documentをelasticsearchにインサート
    db = ElasticVectorSearch.from_documents(docs, embeddings, 
                                            elasticsearch_url=os.environ.get('ELASTICSEARCH_URL'),
                                            index_name="document_test")
