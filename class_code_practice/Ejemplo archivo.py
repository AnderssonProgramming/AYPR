def main():

    archi = open("archivolista.txt", "w")
    for i in range(3):
        palabra=input("Digite palabra")
        archi.write(palabra)
        archi.write("\n")
    archi.close()
    
    
    #Abre el archivo para escribir, sino existe lo crea.
    archivo = open("Prueba.txt","w")

    #Escribe en el archivo la palabra Hola
    archivo.write("Hola")
    archivo.write("\n")

    #Cierra el archivo
    archivo.close()

    #Abre el archivo para añadir al final
    arch = open("Prueba.txt","a")

    arch.write("OtroHola mundo")
    arch.write("\n")
    arch.close()


    
    #Ejemplo escribiendo los elementos de una lista en el archivo
    lista = ["xxxx", "yyyy", "zzzzz", "wwwww", "aaaaa"]
    archivo = open("Prueba.txt", "a")
  
    
    for palabra in lista:
        archivo.write(palabra)
        archivo.write("\n")
    
    archivo.close()

    print("\narchivo completo con segundo ejemplo")

    archivo = open("Prueba.txt", 'r')    
    #imprime el archivo completo
    print(archivo.read())
    archivo.close()

    
    #Ejemplo leyendo del archivo e insertándolo en una lista
    fichero = open("archivolista.txt", "r")
    listanombres = []

    for linea in fichero.readlines():
        print("Esta es linea antes del rstrip",linea)
        lineaaux=linea.rstrip("\n")
        
        listanombres.append(lineaaux)#Aquí hacer la prueba..
        #listanombres.append(linea)

    fichero.close()

    #Imprime lista
    print("\nLista que acaba de leer de archivolista\n")
    print(listanombres)
    
    for nombre in listanombres:
        print (nombre)
    


main()