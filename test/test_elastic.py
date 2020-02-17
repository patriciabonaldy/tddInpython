import unittest
from app.elastic import Elastic
from app.guardar import Guardar

class TddInPythonExample(unittest.TestCase):

     def test_verifica_conex_en_elastic(self):
         elastic = Elastic()
         data =elastic.get_status()
         elastic.close_conect()
         self.assertIsNotNone(data)

     def test_verifica_user(self):
         guardar = Guardar()
         users = guardar.users
         self.assertIsNotNone(users)

     def test_guardar_en_elastic(self):
         guardar = Guardar()
         response = guardar.bulk_user()
         if response:
            self.assertTrue(response)
         else:
            self.assertIsNotNone(response)   


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(TddInPythonExample())