
'''Importamos la inittest
Nos permite realizar pruebas unitarias sin mucho esfuerzo'''
import  unittest 
#Enlazamos con el .py a realizar las pruebas unitarias
from BFS import graph_

from agente import Search
# dicionarios para evaluar la funcion buscar
objetivo = {'Gallinas': '0',
 'Perros': '0', 
 'Cerdos': '0',
 'Burros': '0',
 'Chivos': '0', 
 'Vacas': '0',
 'Conejos':'0',
 'Patos': '0',
 'Ovejas': '0' } 

'''
Comprueba una respuesta específica a un conjunto particular de entradas. 
unittest proporciona una clase base.
------------------------------------
TestCase, que se puede usar para crear nuevos casos de prueba. Banco de pruebas.
'''
class check(unittest.TestCase):
    
    '''
    Comprobamos que nuestro agente cumpla la cantidad del objetivo con el costo final
    '''
    def test_agent(self):
        g = Search(objetivo)
        self.assertEqual(g ,18)

if __name__ == "__main__":
    unittest.main()
    