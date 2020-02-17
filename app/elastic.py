from elasticsearch import Elasticsearch
from elasticsearch.exceptions import TransportError
from elasticsearch.helpers import bulk, streaming_bulk
import json

class Elastic(object):
 
    def __init__(self):
        self.es = Elasticsearch("localhost:9200")

    def get_status(self):
        return json.dumps(self.es.info())

    def close_conect(self):
        self.es.transport.close()

    def get_conection(self):
        conex = self.es.transport.get_connection()
        return conex

    def gendata(self, index, doc):
        yield {
            "_index": index,
            "_type": "_doc",
            "_source": doc,
        }    
    
    def bulk_data(self, index, data):
        try:
            for d in data:
                doc = d            
                bulk(self.es, self.gendata(index, doc))
            return True    
        except SyntaxError as error:
            print(error)
            return False
        except Exception as exception:
            print(exception)  
            return False  
