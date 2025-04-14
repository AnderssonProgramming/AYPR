MAXFI=20
MAXCOL=20


def pedir_tam(dato):
    tam=-1

    if dato=="filas":
        while tam <= 0 or tam > MAXFI:
            tam=int(input("Digite el tamaño: "))
    
    else:
        while tam <= 0 or tam > MAXCOL:
            tam=int(input("Digite el tamaño: "))
    
    return tam

def crear_inicializar():

    matriz=[[0 for nf in range (MAXFI)]for nc in range (MAXCOL)]

    return matriz

def llenarMatriz(nf,nc,matriz):

    for f in range (0,nf):
        for c in range (0,nc):
            print("(",f,",",c,") =",end = " ")
            matriz [f][c]=int(input( ))

def sumaElemFila2(nc,matriz):

    suma=0
    
    for c in range (0,nc):
        suma=suma+matriz[1][0]
    
    return suma

def mostrar (matriz,nf,nc,suma):
    print("\n\n", " R e s u l t a d o s ".center(60, ":"))
    print("\nMatriz: ")

    #Muestro la matriz
    mostrarMat(matriz,nf,nc)

    #Muestro la suma
    print("\n La suma de los elementos de la matriz es: ",suma)

def mostrarMat(matriz,nf,nc):
    for f in range (0,nf):
        for c in range (0,nc):
            print(format(matriz[f][c],"3d"),end= " ")
        
        print("\n", end= " ")
def main():

    print("Bienvenido")
    
    #Pedir tamaño de las matrices
    print("Número de filas de su matriz")

    nf=pedir_tam("filas")
    print("Número de columnas de su matriz")
    nc=pedir_tam("columnas")

    matriz=crear_inicializar()
    #Llenar la matriz
    llenarMatriz(nf,nc,matriz)

    #Sumar los elementos de la matriz
    suma=sumaElemFila2(nf,nc,matriz)

    #Mostrar resultados
    mostrar(matriz,nf,nc,suma)

    print("Bye bye")

main()