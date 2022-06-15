'''
Lo principal para el desarollo del agente es definir el objetivo o la meta
en este caso, se utiliza un diccionario donde ponemos las locaciones con sus
respectivos estados, y como se espera que esten cada una de ellas para que el
agente cumpla con su objetivo.
Locaciones: Gallinas, Perros, Cerdos, Burros, Chivos, Vacas, Conejos
Patos, Ovejas
Estados: 0->bien alimentado.
         1->mal alimentado.
'''
#Creación del diccionario de objetivo que almacena las locaciones y el estado objetivo de cada 1.
objetivo = {'Gallinas': '0',
 'Perros': '0', 
 'Cerdos': '0',
 'Burros': '0',
 'Chivos': '0', 
 'Vacas': '0',
 'Conejos':'0',
 'Patos': '0',
 'Ovejas': '0' } 
#Diccionario vacio para validacion
objetivo_01={}
#Función para verificar si el elemento ingresado esta dentro del diccionario
def verificar_existencia(objetivo_01):
    '''
    Función para indicar que diccionario esta vacio
    Parametros:
    objetivo_01
    Excepciones:
    Evalua si el diccionario es igual a cero
        añade a T el diccionario vacio
        Imprime un mensaje que el diccionario esta vacio
    Retorna:
    Que T esta en 0
    '''
    T = []#lista vacia
    if len(objetivo_01)==0:#evalua si el diccionario es igual a cero
        T.append('Diccionario vacio')#añade a T el diccionario vacio
        print('Diccionario vacio')#imprime un mensaje que el diccionario esta vacio
    return(T[0])  #retorna que T esta en 0
#Función para buscar las locaciones y verificar que los estados cumplan con el objetivo del agente 
def  Buscar(objetivo): 
    '''
    Función que permite buscar las locaciones y verificar que cumplan 
    con los estados para llegar al objetivo del agente.
    Parametros:
    objetivo
    Excepciones:
    Imprime mensaje de aviso.
    Evalua:for t in objetivo 
        Imprime mensaje que indica los animales que existen en la granja, estan dentro del diccionario
    pide ingresar el animal 
    costo se inicializa en 0
    Evalua:si el animal ingresado esta en la lista 
        imprime que el animal existe
        pide que ingrese el estado del animal
            Evalua: for n in objetivo (para cada elemento en la lista de objetivos)
                Agrega un elemento al final de la lista
            Evalua: for n in lista(para cada elemento animal en la lista que contiene los objetivos)
                Evalua: Si Animal ==n (si el elemento de la lista es igual al ingresado)
                    Para que no repita en input al ingresar los estados posteriormente
                    Si son iguales los remueve
                    Array vacio para guardar los otros estados de los animales y evaluarlos despues
                    Imprime el diccionario de objetivos
                    Evalua: for t in nueva_lista(para cada elemento animal en la lista que contiene los objetivos)
                        Solicita los estados de los demas animales
                        Guarda el valor ingresado al final de la lista
                        Agrega el elemento  por consola
                        Crea un nuevo diccionario con los estados y animales agregados cada input
                        Imprime mensaje 
                        Evalua: Si estado == '0' (Si el estado ingresado es igual al estado 0)
                            Imprime si el animal esta alimentado
                            Evalua:for animals in new_lista(para saber si los otros animales estan alimentados o no)
                                Evalua: Si nuevo_diccionario[animals]== '1'(Para cada animal que no se alimentado)
                                    imprime mensaje animal iterado no tienen comida
                                    Imprime mensaje de que alimentara al animal iterado
                                    Asigna el costo por animal evaluado
                                    Imprime mensaje respecto al costo
                                    Cambia el estado
                                    Aumenta el costo
                                    Imprime costo actualizado
                                    Imprime mensaje de verificacion del animal
                                Caso contrario:
                                    Imprime mensaje sobre los animales que tienen comida
                                    Imprime animal alimentado y el costo se mantiene
                        Evalua: Si Si estado == '1'
                            Imprime que el animal no esta alimentado
                            Evalua:for animals in new_lista(para saber si los otros animales estan alimentados o no)
                                Evalua: Si nuevo_diccionario[animals]== '1'(Para cada animal que no se alimentado)
                                    imprime mensaje animal iterado no tienen comida
                                    Imprime mensaje de que alimentara al animal iterado
                                    Asigna el costo por animal evaluado
                                    Imprime mensaje respecto al costo
                                    Cambia el estado
                                    Aumenta el costo
                                    Imprime costo actualizado
                                    Imprime mensaje de verificacion del animal
                                Caso contrario:
                                    Imprime mensaje sobre los animales que tienen comida
                                    Imprime animal alimentado y el costo se mantiene
    caso contrario
        imprime mensaje avisando que animal ingresado no existe
        costo=0
    Retorna:
    retorna el costo
    '''
    print('los animales en esta granja son: ')#Mensaje de aviso
    for t in objetivo:#Busca si los animales dentro de objetivos
        print(f'En la granja existen {t}')#Imprime los animales que estan dentro de la granja
    Animal = input('Ingrese nombre de uno de los animales: ')#pide al usuario que ingrese uno de los animales
    costo = 0 #inicializa el costo en 0
    if f'{Animal}' in objetivo: #evalua si el animal ingresado se encuentra en el diccionario
        print('Este animal si existe')#mensaje que indica que el animal ingresado existe
        estado = int(input("Ingrese el estado del " +Animal+ ":\n "))#pide que ingrese el estado del animal ingresado
        while estado<0 or estado>1: #Evalua estado
            print(f'Ingrese nuevamente el estado de {Animal} ')#pide que ingrese estado
            estado = int(input('\nEscriba 1 si esta mal alimentado o 0 si esta bien alimentado: '))
        estado  = str(estado)
        lista = []#lista vacia para agregar los indices del diccionario
        for n in objetivo:#Recorre buscando si n esta en el diccionario objetivo
            lista.append(n) #agrega n a lista vacia
        for n in lista: #recorre si n esta en la lista de los objetivos
            if Animal ==n: #evalua si n es igual al animal ingresado
                nueva_lista = lista #medida para no repetir el input
                nueva_lista.remove(n)#si esta repetido lo elimina
                lista_estados=[] #lista para ir añadiendo los estados 
                for t in nueva_lista:#evalua t en la nueva lista 
                    A=int(input(f'Ingrese el estado de {t}:\n '))#Solicita que ingrese el estado
                    while A<0 or A>1:#va comprobando si el estado es 1 o 0
                        print(f'Ingrese nuevamente el estado de {t}')#pide ingresar estado
                        A = int(input('\nEscriba 1 si esta mal alimentado o 0 si esta bien alimentado: '))#imprime mensaje
                    A = str(A)   
                    lista_estados.append(A) #Agrega y guarda t en la lista de estados
                    lista_nueva = [str(Animal)] +nueva_lista #indica que lista nueva es el animal ingresado y la nueva lista
                    nuevo_diccionario = dict(zip(lista_nueva, [str(estado)] + lista_estados))#creamos un nuevo dicionario con los animales y los estados que hemos agregado en cada input
                print(f"--------- Evaluacion de alimentacion de {n}------")   #evaluacion de la alimentacion
                if estado == '0':#evalua si el estado ingresado es 0
                    print(f'{n} Alimentados ') #imprime mensaje de animal alimentado
                    for animal in lista_nueva:#evalua para conocer si los demas animales del diccionario se encuentran alimentados
                        if  nuevo_diccionario[animal]== '1':#si el animal no esta alimentado
                            print(f"Los {animal} No tienen comida") #imprime mensaje que ese animal no tiene comida
                            print(f"Se alimentará {animal}")#avisa que el animal se va alimentar
                            costo += 1 #indica costo va aumentar
                            print("El costo actual es: " +str(costo))#imprime que el costo sctual
                            objetivo[animal] ='0' #cambio de estado
                            costo += 1 #aumento de costo
                            print(f"se ha vuelto a verificar la comida de {animal}")#mensaje que indica que se volvio a verificar la comida del animal
                            print("El costo actual es: "  +str(costo)) #imprime el costo actual
                        else: #caso contrario
                            print(f"Los {animal} tienen comida")#indica que el animal tiene comida
                            print(f"{animal} alimentados , no se aumenta costo, este se mantiene en se mantiene en: "  + str(costo)) #indica que como el animal ya esta alimentado el costo se mantiene
                elif estado == '1':# Evalua si el estado ingresado es igual a 1
                    print(f'{n} NO Alimentados ')#indica que el animal no esta alimentado
                    for animal in lista_nueva: #evalua para conocer si los demas animales del diccionario se encuentran alimentados    
                        if  nuevo_diccionario[animal]== '1':#verifica en el diccionario nuevo si no esta alimentado
                            print(f"Los {animal} No tienen comida")#avisa que el animal se va alimentar
                            print(f"Se alimentará {animal}") #avisa que el animal se va alimentar
                            costo += 1  #indica costo va aumentar
                            print("El costo actual es: " +str(costo)) #imprime que el costo sctual               
                            objetivo[animal] ='0' #cambio de estado
                            costo += 1  #aumento de costo
                            print(f"se ha vuelto a verificar la comida de {animal}")#mensaje que indica que se volvio a verificar la comida del animal
                            print("El costo actual es: "  +str(costo))#imprime el costo actual
                        else:  #caso contrario
                            print(f"Los {animal} tienen comida")#indica que el animal tiene comida
                            print(f"{animal} alimentados , no se aumenta costo, este se mantiene en se mantiene en: "  + str(costo)) #indica que como el animal ya esta alimentado el costo se mantiene
                else:#caso sontrario
                    print(f'{n} No alimentados ')#imprime que el animal no esta alimentado
    else :#casocontrario
        print('Este animal no existe en esta granja, intente otra vez')#indica mensaje que animal ingresado no esta en el diccionario que lo intente de nuevo
        costo = 'Este animal no existe'
        #costo = 0#el costo sigue en 0
    return(costo)#retorna el costo
if __name__ == "__main__":#clase main
    Buscar(objetivo)#llama a la función buscar
    verificar_existencia(objetivo_01)#llama a la funcion para verificar la existencia

                       