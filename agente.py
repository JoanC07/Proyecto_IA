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