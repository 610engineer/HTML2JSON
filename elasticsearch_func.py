import os
import env
from elasticsearch import Elasticsearch

def add_document(document):
    # Elasticsearchエンドポイント
    es = Elasticsearch(os.environ.get('ELASTICSEARCH_URL'))

    # testdocument
    res = es.index(index = "test",
            document=document
    )

    print(res)

    es.close()

def get_document(id):
    # Elasticsearchエンドポイント
    es = Elasticsearch(os.environ.get('ELASTICSEARCH_URL'))
    res = es.search(index=id
                )

    es.close()

    return res