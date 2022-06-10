objetivo = {'Gallinas': '0',
 'Perros': '0', 
 'Cerdos': '0',
 'Burros': '0',
 'Chivos': '0', 
 'Vacas': '0',
 'Conejos':'0',
 'Patos': '0',
 'Ovejas': '0' } 

def  Buscar(objetivo):
    print('Elementos')
    print(objetivo)
    costo = 0 
    Animal = input("Ingrese el nombre del animal: ") 
    estado = input("Ingrese el estado del " +Animal+ ": ")
    lista = []
    for n in objetivo:
        lista.append(n) 
        for n in lista:
            if Animal ==n:
                nueva_lista = lista
                nueva_lista.remove(n)
            lista_estados=[] 
            print("Objetivo:" + str(objetivo))
            for t in nueva_lista:
                t=input(f'Ingrese el estado de {t}: ')
                lista_estados.append(t) 
                lista_nueva = [str(Animal)] +nueva_lista 
                nuevo_diccionario = dict(zip(lista_nueva, [str(estado)] + lista_estados))
            print(f"--------- Evaluacion de alimentacion de {n}------")   
            if estado == '0':
                print(f'{n} Alimentados ')
                for animales in nueva_lista:
                    if  nuevo_diccionario[animales]== '1':
                        print(f"Los {animales} No tienen comida")
                        print(f"Se alimentará {animales}")
                        costo += 1 #
                        print("El costo actual es: " +str(costo))
                        objetivo[animales] ='0' 
                        costo += 1 
                        print(f"se ha vuelto a verificar la comida de {animales}")
                        print("El costo actual es: "  +str(costo)) 
                    else: 
                        print(f"Los {animales} tienen comida")
                        print(f"{animales} alimentados , no se aumenta costo, este se mantiene en se mantiene en: "  + str(costo))
            elif estado == '1':
                print(f'{n} NO Alimentados ')
                for animales in nueva_lista:     
                    if  nuevo_diccionario[animales]== '1':
                        print(f"Los {animales} No tienen comida")
                        print(f"Se alimentará {animales}") 
                        print("El costo actual es: " +str(costo))                   
                        objetivo[animales] ='0' 
                        costo += 1 
                        print(f"se ha vuelto a verificar la comida de {animales}")
                        print("El costo actual es: "  +str(costo))
                    else:  
                        print(f"Los {animales} tienen comida")
                        print(f"{animales} alimentados , no se aumenta costo, este se mantiene en se mantiene en: "  + str(costo)) #Costo se mantiene  
            else:
                print(f'{n} No alimentados ')
                       