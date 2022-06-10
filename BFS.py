
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
