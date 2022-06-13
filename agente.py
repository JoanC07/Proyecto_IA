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
    T = []#lista vacia
    if len(objetivo_01)==0:
        T.append('Diccionario vacio')
        print('Diccionario vacio')
    return(T[0])  
#Función 
def  Buscar(objetivo): 
    '''
    Función que permite buscar las locaciones y verificar que cumplan 
    con los estados para llegar al objetivo del agente.
    Parametros:
    objetivo
    Estado
    lista[]->lista vacia para agregar los indices del diccionario
    Excepciones:
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
    '''
    print('los animales en esta granja son: ')
    for t in objetivo:
        print(f'En la granja existen {t}')
    Animal = input('ingrese nombre de uno de los animales : ')
    costo = 0
    if f'{Animal}' in objetivo:
        print('Este animal si existe')
        estado = input("Ingrese el estado del " +Animal+ ": ")
        lista = []
        for n in objetivo:
            lista.append(n) 
        for n in lista:
            if Animal ==n:
                nueva_lista = lista
                nueva_lista.remove(n)
                lista_estados=[] 
                for t in nueva_lista:
                    t=input(f'Ingrese el estado de {t}: ')
                    lista_estados.append(t) 
                    lista_nueva = [str(Animal)] +nueva_lista 
                    nuevo_diccionario = dict(zip(lista_nueva, [str(estado)] + lista_estados))
                print(f"--------- Evaluacion de alimentacion de {n}------")   
                if estado == '0':
                    print(f'{n} Alimentados ')
                    for animal in lista_nueva:
                        if  nuevo_diccionario[animal]== '1':
                            print(f"Los {animal} No tienen comida")
                            print(f"Se alimentará {animal}")
                            costo += 1 
                            print("El costo actual es: " +str(costo))
                            objetivo[animal] ='0' 
                            costo += 1 
                            print(f"se ha vuelto a verificar la comida de {animal}")
                            print("El costo actual es: "  +str(costo)) 
                        else: 
                            print(f"Los {animal} tienen comida")
                            print(f"{animal} alimentados , no se aumenta costo, este se mantiene en se mantiene en: "  + str(costo))
                elif estado == '1':
                    print(f'{n} NO Alimentados ')
                    for animal in lista_nueva:     
                        if  nuevo_diccionario[animal]== '1':
                            print(f"Los {animal} No tienen comida")
                            print(f"Se alimentará {animal}") 
                            costo += 1 
                            print("El costo actual es: " +str(costo))                   
                            objetivo[animal] ='0' 
                            costo += 1 
                            print(f"se ha vuelto a verificar la comida de {animal}")
                            print("El costo actual es: "  +str(costo))
                        else:  
                            print(f"Los {animal} tienen comida")
                            print(f"{animal} alimentados , no se aumenta costo, este se mantiene en se mantiene en: "  + str(costo)) #Costo se mantiene  
                else:
                    print(f'{n} No alimentados ')
    else :
        print('Este animal no existe en esta granja ')
        #costo = 'Este animal no existe'
        costo = 0
    return(costo)
if __name__ == "__main__":
    Buscar(objetivo)
    verificar_existencia(objetivo_01)

                       