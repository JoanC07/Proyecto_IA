'''
Importamos la inittest
Nos permite realizar pruebas unitarias sin mucho esfuerzo
'''
import  unittest 
#Enlazamos con el .py a realizar las pruebas unitarias
from BFS import grafo_ , verificar_nodo
'''
Comprueba una respuesta específica a un conjunto particular de entradas. 
unittest proporciona una clase base.
------------------------------------
TestCase, que se puede usar para crear nuevos casos de prueba. Banco de pruebas.
'''
class check(unittest.TestCase): #Clase Cheak
    
    #Probamos el grafo ingresado manualmente del py BFS
    def test_grafo(self): #Sentencia para el test
        grafo = grafo_() #Verificacion del grafo
        self.assertEqual(grafo ,[1, 0, 2, 6])#Recorrido a esperar
    
    #Revisamos si los nodos estan dentro del rango 
    def test_verficacion(self): #Sentencia para el test
        verificado = verificar_nodo() #Verificacion del nodo
        self.assertEqual(verificado,'Nodos dentro rango')#Mensaje dentro del rango

if __name__ == "__main__":
    unittest.main()
           
    