import os
import env
from elasticsearch import Elasticsearch

# Elasticsearchエンドポイント
es = Elasticsearch(os.environ.get('ELASTICSEARCH_URL'))

# testdocument
es.index(index = "test",
            id = 2,
            document={"key": "bbb", "value": "test2"})

res = es.search(index="test"
                )

print(res)
