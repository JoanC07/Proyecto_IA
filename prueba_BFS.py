'''
Importamos la inittest
Nos permite realizar pruebas unitarias sin mucho esfuerzo
'''
import  unittest 
#Enlazamos con el .py a realizar las pruebas unitarias
from BFS import grafo_
'''
Comprueba una respuesta específica a un conjunto particular de entradas. 
unittest proporciona una clase base.
------------------------------------
TestCase, que se puede usar para crear nuevos casos de prueba. Banco de pruebas.
'''
class check(unittest.TestCase):
    
    #Probamos el grafo ingresado manualmente del py BFS
    def prueba_grafo(self):
        grafo = grafo_(1, 6)
        
        self.assertEqual(grafo ,[1, 0, 2, 9])

if __name__ == "__main__":
    unittest.main()
           
    