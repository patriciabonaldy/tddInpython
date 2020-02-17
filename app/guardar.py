from app.elastic import Elastic
from app.users import get_Users


class Guardar():

    def __init__(self):
        self.users = get_Users()
        self.es    = Elastic()

    def bulk_user(self):
        return self.es.bulk_data("users", self.users)
           
#g = Guardar()
#g.bulk_user()
