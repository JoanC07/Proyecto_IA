
import matplotlib.pyplot as plt
import networkx as nx

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

nueva = []
for n in  F:
    nueva.append(n)
nueva.sort()

llave_nueva = []
for i in nueva:
    llave =(F[i])
    llave.sort()
    llave_nueva.append(llave)

clasificar_diccionario = dict(zip(nueva,llave_nueva))
print(clasificar_diccionario)
T = nx.Graph(clasificar_diccionario)
nx.draw_networkx(T)
plt.plot

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
        # Set of visitado nodos to prevent loops
        visitado = set()
        cola = Queue()
    
        # Add the nodo_de_inicio to the queue and visitado list
        cola.put(nodo_de_inicio)
        visitado.add(nodo_de_inicio)
        
        # nodo_de_inicio has not padres
        padre = dict()
        padre[nodo_de_inicio] = None
         # Perform step 3
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