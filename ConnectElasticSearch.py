from elasticsearch import Elasticsearch

# Elasticsearchエンドポイント
es = Elasticsearch("http://localhost:9200")

# testdocument
es.index(index = "test",
            id = 2,
            document={"key": "bbb", "value": "test2"})

res = es.search(index="test"
                )

print(res)
