'''
Importamos la libreria matplotlib y networks

'''
import matplotlib.pyplot as plt
import networkx as nx
'''
Codigo semi dinamico, tenemos un diccionario de datos 
Pasamos de letras a numeros.
'''
F = {
    '0' :['1','2','4','7','3','5'],
    '1' :['0','7','15','9'],
    '2' :['0','5','6','14'],
    '3' :['0','14','7'],
    '4' :['0','5','19','11','10','9'],
    '5' :['0','2','12','4'],
    '6' :['2','13'],
    '7' : ['3','0','1','15'],
    '8' : ['15','9','16'],
    '10' : ['4','9','11','18'],
    '11' : ['4','10'],
    '12' : ['5','19','13'],
    '13' : ['6','12'],
    '14' : ['3','2'],
    '15' : ['8','7','1'],
    '16' : ['8','9','17'],
    '17' : ['16','18'],
    '18' : ['10','17'],
    '19' : ['12','4'],
    '9' :['16','8','10','4']
    
    } 
'''
Bucles para ordenar nuestro diccionario
'''
nueva = []
for n in  F:
    nueva.append(n)
nueva.sort()

llave_nueva = []
for i in nueva:
    llave =(F[i])
    llave.sort()
    llave_nueva.append(llave)
#Diccionario ordenado
clasificar_diccionario = dict(zip(nueva,llave_nueva))
print(clasificar_diccionario)
#Creacion de la clase T mediante la funcion del grafo
T = nx.Graph(clasificar_diccionario)
#Graficamos el grafo
nx.draw_networkx(T)
#Imprimimos nuestro grafo
plt.plot
'''
Importamos Queue
'''
from queue import Queue


class Grafo:
    def __init__(self, m_numero_nodos, dirigido=True):
        self.m_m_numero_nodos = m_numero_nodos 
        self.m_nodos = range(self.m_m_numero_nodos) 
        self.m_dirigido = dirigido
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}      
	
    def agregar_borde(self, nodo1, nodo2, peso=1):
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))

        if not self.m_dirigido:
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
    def Imprimir_lista_adyacencia(self):
        for llave in self.m_lista_adyacencia.keys():
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def bfs(self, nodo_de_inicio, nodo_objetivo):

        visitado = set()
        cola = Queue()
    

        cola.put(nodo_de_inicio)
        visitado.add(nodo_de_inicio)
        

        padre = dict()
        padre[nodo_de_inicio] = None

        camino_encontrado = False
        while not cola.empty():
            nodo_actual = cola.get()
            if nodo_actual == nodo_objetivo:
                camino_encontrado = True
                break
    
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                if siguiente_nodo not in visitado:
                    cola.put(siguiente_nodo)
                    padre[siguiente_nodo] = nodo_actual
                    visitado.add(siguiente_nodo)
                camino = []
        if camino_encontrado:
            camino.append(nodo_objetivo)
            while padre[nodo_objetivo] is not None:
                camino.append(padre[nodo_objetivo]) 
                nodo_objetivo = padre[nodo_objetivo]
            camino.reverse()
        return camino 
grafo = Grafo(20, dirigido=False)
# Nodo 1
grafo.agregar_borde(0, 1)
grafo.agregar_borde(0, 2)
grafo.agregar_borde(0, 3)
grafo.agregar_borde(0, 4)
grafo.agregar_borde(0, 5)
grafo.agregar_borde(0, 7)
# Nodo 2
grafo.agregar_borde(1, 0)
grafo.agregar_borde(1, 7)
grafo.agregar_borde(1, 9)
grafo.agregar_borde(1, 15)
#Nodo 3
grafo.agregar_borde(2, 0)
grafo.agregar_borde(2, 5)
grafo.agregar_borde(2, 6)
grafo.agregar_borde(2, 14)
#Nodo 4
grafo.agregar_borde(3, 0)
grafo.agregar_borde(3, 7)
grafo.agregar_borde(3, 14)
#Nodo 5
grafo.agregar_borde(4, 0)
grafo.agregar_borde(4, 5)
grafo.agregar_borde(4, 9)
grafo.agregar_borde(4, 10)
grafo.agregar_borde(4, 11)
grafo.agregar_borde(4, 19)
#Nodo 6
grafo.agregar_borde(5, 0)
grafo.agregar_borde(5, 2)
grafo.agregar_borde(5, 4)
grafo.agregar_borde(5, 12)
#Nodo 7
grafo.agregar_borde(6, 2)
grafo.agregar_borde(6, 13)
#Nodo 8
grafo.agregar_borde(7, 0)
grafo.agregar_borde(7, 1)
grafo.agregar_borde(7, 3)
grafo.agregar_borde(7, 15)
#Nodo 9
grafo.agregar_borde(8, 9)
grafo.agregar_borde(8, 15)
grafo.agregar_borde(8, 16)
#Nodo 10
grafo.agregar_borde(9, 4)
grafo.agregar_borde(9, 8)
grafo.agregar_borde(9, 10)
grafo.agregar_borde(9, 16)
#Nodo 11
grafo.agregar_borde(10,4)
grafo.agregar_borde(10,9) 
grafo.agregar_borde(10,11)
grafo.agregar_borde(10,18)
#Nodo 12
grafo.agregar_borde(11,4)
grafo.agregar_borde(11,10) 
#Nodo 13
grafo.agregar_borde(12,5)
grafo.agregar_borde(12,13) 
grafo.agregar_borde(12,19)
#Nodo 14
grafo.agregar_borde(13,6)
grafo.agregar_borde(13,12) 
#Nodo 15
grafo.agregar_borde(14,2)
grafo.agregar_borde(14,3) 
#Nodo 16
grafo.agregar_borde(15,1)
grafo.agregar_borde(15,7) 
grafo.agregar_borde(15,8)
#Nodo 17
grafo.agregar_borde(16,8)
grafo.agregar_borde(16,9) 
grafo.agregar_borde(16,17)
#Nodo 18
grafo.agregar_borde(17,16)
grafo.agregar_borde(17,18)
#Nodo 19 
grafo.agregar_borde(18,10) 
grafo.agregar_borde(18,17)
#Nodo 20
grafo.agregar_borde(19,4) 
grafo.agregar_borde(19,12)  

grafo.Imprimir_lista_adyacencia()


A = int(input('Escriba el Nodo Incial: '))

B = int(input('Escriba el Nodo Final: '))
camino = grafo.bfs(A,B)

print(f'el camino mas  corto de {A} hacia {B} es : ')
print(camino)