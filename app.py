
# -*- coding: utf-8 -*-
import glob
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from elasticsearch_func import add_document
from langchain.document_loaders import UnstructuredHTMLLoader, DirectoryLoader
from html2vectorstore import html_loader

import os
import env

def main():

    print("INPUT FOLDER PATH")
    folder_path = input()

    # test PATH
    folder_path = os.environ.get('TEST_PATH')

    # ログ表示
    print(folder_path)

    # 読み込むファイルの拡張子を指定
    types = ("html", "htm")
    files = []

    # 拡張子の数だけfilesの配列を作成
    for type in types:
        files += glob.glob(folder_path + "\*." + type)

    # フォルダの中身を取得
    for file in files:
        # ログ表示

        print(file)

        # ファイルの中身がない場合は次のファイルへ
        f = open(file,  encoding="utf-8").read()
        # print("F," , f)

        if f == "":
            continue

        # HTMLLoaderで変換
        documents = html_loader(file)

        # elasticsearchに入れるために分割
        text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
        docs = text_splitter.split_documents(documents)
        embeddings = OpenAIEmbeddings()

        # documentをelasticsearchにインサート
        db = ElasticVectorSearch.from_documents(docs, embeddings, 
                                                elasticsearch_url=os.environ.get('ELASTICSEARCH_URL'),
                                                index_name="document_test")
    
    """
    # クエリ
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