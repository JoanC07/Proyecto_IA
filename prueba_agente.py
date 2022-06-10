
'''
Importacion de librerias para prueba unitarias
de archivo py correspondiente al agente
Crea dicionarios para evaluar la funcion Buscar
'''
import  unittest 
from agente import Buscar
# 
objetivo = {'Gallinas': '0',
 'Perros': '0', 
 'Cerdos': '0',
 'Burros': '0',
 'Chivos': '0', 
 'Vacas': '0',
 'Conejos':'0',
 'Patos': '0',
 'Ovejas': '0' } 

class prueba(unittest.TestCase):
    '''Clase prueba 
    metodo prueba_agente
        instanciamos la funcion que se va evaluar
        con la funcion de unittest(parametros para evaluar)
    '''   
    def prueba_agente(self):
        g = Buscar(objetivo)
        self.assertEqual(g ,18)
if __name__ == "__main__":
    unittest.main()
    