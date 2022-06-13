'''
Importamos las librerias 
matplotlib la cual nos permitirá graficar nuestro grafo a partir de nuestro diccionario de datos
y networks.

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
    '7' :['3','0','1','15'],
    '8' :['15','9','16'],
    '10' :['4','9','11','18'],
    '11' :['4','10'],
    '12' :['5','19','13'],
    '13' :['6','12'],
    '14' :['3','2'],
    '15' :['8','7','1'],
    '16' :['8','9','17'],
    '17' :['16','18'],
    '18' :['10','17'],
    '19' :['12','4'],
    '9' :['16','8','10','4']
    
    } 
'''
Bucles para ordenar nuestro diccionario
'''
nueva = [] #Nueva lista vacia
for n in  F: #Definimos nuestro diccionario como n
    nueva.append(n)
nueva.sort()

llave_nueva = [] #nueva llave vacia
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
'''
    Clase Grafo la cual nos va a representar a nuestro Grafo.

    ...

    Parametros
    ----------
        m_numero_nodos : int
            Numero de nodos 
        numero_nodos : int
            Rango de nodos 
        m_dirigido : boolean
            Tipo de grafo si es dirigida o no dirigida.
        m_lista_adyacencia : diccionario
            Representación gráfica - Lista de adyacencia.
    Establecimiento de los parametros para el metodo constructor (inicializado)

    Métodos
    ------- 
        Agregar_borde(self, nodo1, nodo2, peso=1):
            Agregar arista al grafo.
        Imprimir_lista_adyacencia(self):
            Imprime la representacion grafica
        __init__(self, numero_nodos, dirigido=True):
            Recibe el numero de nodos y rango y verifica si es dirigido o no
        bfs(nodo_inicial):
            Imprimir el recorrido BFS de un vértice fuente dado.

    '''

class Grafo:
    def __init__(self, m_numero_nodos, dirigido=True):
        '''
        Recibe el numero de nodos de nuestra clase principal Grafos. 

        Parametros.
            m_numero_nodos : int
                 Numero de nodos 
            numero_nodos : int
                Rango de nodos 
            m_dirigido : boolean
                Tipo de grafo si es dirigida o no dirigida.
            m_lista_adyacencia : diccionario
             Representación gráfica - Lista de adyacencia.
        '''
        #Numero de Nodos
        self.m_m_numero_nodos = m_numero_nodos 
        # Rango de nodos
        self.m_nodos = range(self.m_m_numero_nodos) 
        # Tipo de grafo si es dirigida o no dirigida
        self.m_dirigido = dirigido
        # Usamos un directorio de datos para implementar una lista de adyacencia.
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}      

    def agregar_borde(self, nodo1, nodo2, peso=1):
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
	
        '''
        Agregar borde al gráfo. 
        Parametros.
        ----------
            nodo1: int
            nodo2: int
            peso: int
            Peso y se agregan a nuestra lista de adyacencia con el nodo que corresponde.
        '''
        #Agrega el nodo 1 a nuestra lista del nodo 2
        if not self.m_dirigido:
            #Agrega el nodo 2 a nuestra lista del nodo 1
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))
    # Imprimir la representación gráfica
    def Imprimir_lista_adyacencia(self):
        '''
        Nos imprime la representacion grafica por pantalla el grafo generado nuestra 
        lista de ayacencia.

        '''
        #Recorre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            #Imprime nuestro nodo
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def bfs(self, nodo_de_inicio, nodo_objetivo):
        '''
        Función que imprime el recorrido BFS de un vértice fuente dado. bfs_traversal(int s) y
        recorre los vértices alcanzables desde s.
        Genera una lista de las colas visitadas y muestra el recorrido realizado, recibe el 
        valor de nodo_de_inicio.

         Añade el nodo_de_inicio a la cola y a la lista de visitas.

        Bucle de los nodos.
            Quitar un vértice de la cola.
            Imprimirlo vertice.
            Obtener todos los vértices adyacentes del vértice de la cola. 
            Si un vértice adyacente ha sido visitado, entonces se marca como visitado y pongalo en cola.
        '''

        # Conjunto de nodos visitados para evitar bucles
        visitado = set()
        cola = Queue()
    
        # Añade el nodo_de_inicio a la cola 
        cola.put(nodo_de_inicio)
        # Agrega a la lista de visitas
        visitado.add(nodo_de_inicio)
        padre = dict()
        padre[nodo_de_inicio] = None
        camino_encontrado = False
        #Bucle de los nodos
        while not cola.empty():
            # Quitar un vértice de la cola
            nodo_actual = cola.get()
            #Verifica si el nodo vecino es igual a nuesto nodo objetivo
            if nodo_actual == nodo_objetivo:
                #Verificamos si el camino esta encontrado
                camino_encontrado = True
                break
            # Obtener todos los vértices adyacentes de la cola. 
            for (siguiente_nodo, peso) in self.m_lista_adyacencia[nodo_actual]:
                #Si un vértice adyacente ha sido visitado
                if siguiente_nodo not in visitado:
                    #Se coloca en la cola
                    cola.put(siguiente_nodo)
                    padre[siguiente_nodo] = nodo_actual
                    #Se marca el nodo
                    visitado.add(siguiente_nodo)
        #Camino de construccion
        '''
        Se añade el nodos a nuestro camino
        Nodo se debe encontrar en la lista padre y que no este marcado.
        '''
        camino = [] #Camino en lista vacia
        if camino_encontrado:
            camino.append(nodo_objetivo)
            '''
            Se agrega a la lista padre o ruta de los elementos que se encuentran
            dentro de la lista padre y nuestro nodo objetivo.

            '''
            while padre[nodo_objetivo] is not None: #Se agrega a la lista padre
                camino.append(padre[nodo_objetivo]) 
                nodo_objetivo = padre[nodo_objetivo] # 
                '''
                Invierte el orden de la lista padre para dejar el ultimo valor 
                al inicio  y el primero al ultimo
                '''
            camino.reverse()
        return camino #retorna el camino

def verificar_nodo():
    
    A = int(input('Ingrese el Nodo A: ')) #Imprime el nodo A
    B = int(input('Ingrese el Nodo B: ')) #Imprime el nodo B
    T =[] #T como vacio
    if A>20: # Condicional si A es mayor que 20
        G = 'Nodo A fuera de rango' # Nos retorna A fuera de rango
        print(G) #Imprime el mensaje en G
        T.append(G)
    elif B > 20: # Condicional si A es mayor que 20
        G = 'Nodo B fuera de rango'  # Nos retorna A fuera de rango
        print(G) #Imprime el mensaje en G
        T.append(G)   
    else:
        G = 'Nodos dentro rango' #Caso contrario esta dentro del rango
        print(G) #Imprime el mensaje en G
        T.append(G) 
        
    return(T[0]) #Retorna nuestra lista

def grafo_(): 
    #Creacion del grafo
    grafo = Grafo(20, dirigido=False)
    #Agregamos 20 nodos a nuestro grafo
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
    #Imprime nuestra lista de adyacencia
    #grafo.Imprimir_lista_adyacencia()
    #Ingreso de los nodos a llegar
    A = int(input('Escriba el Nodo Incial: ')) # Se escribe el nodo inicial 
    B = int(input('Escriba el Nodo Final: ')) # Se escribe nuestro nodo objetivo

    camino = grafo.bfs(A,B)
    #Nos imprime la ruta mas corta
    print(f'el camino mas  corto de {A} hacia {B} es : ')
    print(camino) #Imprime la variable
    return(camino)  # Retorna camino del grafo

if __name__ =="__main__":
    
    grafo_() #Para vailidar en test si el recorrido es el correcto
    verificar_nodo() #Para vailidar en nodo es correcto