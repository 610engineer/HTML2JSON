# Elasticsearchエンドポイント
es = Elasticsearch("http://localhost:9200/")

# test
es.index(index = "test",
            doc_type='_doc',
            id = 1,
            body={"key": "aaa", "value": "test"})

res = es.get(index="test",
                doc_type = '_doc',
                id = 1)['_source']

print(es)