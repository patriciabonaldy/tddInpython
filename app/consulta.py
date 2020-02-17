from elasticsearch import Elasticsearch

es = Elasticsearch("localhost:9200")

class Consultas():

    def __init__(self):
        self.search_all = {
                "query": 
                {
                    "match_all": {}
                }
            }

    def buscar_all(self):
        res = es.search(index="users",body=self.search_all)
        print(res)
        for hit in res['hits']['hits']:
           print("%(contenido)s %(cantidad)s %(fecha_expiracion)d" %hit['_source'])
           

