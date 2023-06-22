
# -*- coding: utf-8 -*-
import glob
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch
from convert_to_utf8_from_shiftJIS import convert_html_files
from langchain.document_loaders import UnstructuredHTMLLoader, DirectoryLoader
from directory_loader import insert_to_elasticsearch

import os
import env

def main():

    print("INPUT FOLDER PATH")
    folder_path = input()

    # test PATH
    # folder_path = os.environ.get('TEST_PATH')

    # ログ表示
    print(folder_path)

    # 現在のディレクトリを取得
    cwd = os.getcwd()

    # 変換ファイルを保存するディレクトリ
    target_dir = cwd + "\converted_files"

    # html/htmファイルをshift-jisからutf-8へ変換
    convert_html_files(folder_path, target_dir)

    # html/htmファイルをElasticsearchへ挿入
    insert_to_elasticsearch(target_dir)

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