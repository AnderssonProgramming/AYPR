MAXFI=20
MAXCOL=20


def matriz_cuadrada(dato):
    tam=-1
    
    if dato =="filas":
        while tam <=0 or tam > MAXFI:
            tam=int(input("Digite el tamaño: "))
    else: 
        while tam <=0 or tam > MAXCOL:
            tam=int(input("Digite el tamaño: "))
    
    
    return tam

def crear_inicializar():

    matriz1=[[0 for nf in range (MAXFI)]for nc in range (MAXCOL)]
    matriz2=[[0 for nf in range (MAXFI)]for nc in range (MAXCOL)]
    
    return [matriz1,matriz2]

def llenarMatriz(nf,nc,matriz1,matriz2):

    for f in range (0,nf):
        for c in range (0,nc):
            print("(",f,",",c,") =",end = " ")
            matriz1 [f][c]=int(input( ))
            print("(",f,",",c,") =",end = " ")
            matriz2 [f][c]=int(input( ))

def sumaMat(nf,nc,matriz1,matriz2):

    suma = [[0 for nf in range (MAXFI)]for nc in range (MAXCOL)]
    for f in range(nf):
        for c in range(nc):
            suma[f][c] = matriz1[f][c] + matriz2[f][c]
    return suma
    
def mostrar (matriz1,matriz2,nf,nc,suma):
    print("\n\n", " R e s u l t a d o s ".center(60, ":"))

    print("\nMatriz 1: ")
    mostrarMat(matriz1, nf, nc)

    print("\nMatriz 2:")
    mostrarMat(matriz2, nf, nc)

    print("\n La suma de las dos matrices es:")
    mostrarMat(suma, nf, nc)

def mostrarMat(matriz,nf,nc):
    for f in range (0,nf):
        for c in range (0,nc):
            print(format(matriz[f][c],"3d"), end= " ")
        
        print("\n", end= " ")

def main():

    print("Bienvenido")
    
    #Pedir tamaño de las matrices
    print("Número de filas de su matriz")

    nf=matriz_cuadrada("filas")
    print("Número de columnas de su matriz")
    nc=matriz_cuadrada("columnas")

    [matriz1,matriz2]=crear_inicializar()
    #Llenar la matriz
    llenarMatriz(nf,nc,matriz1,matriz2)

    #Sumar matrices
    suma=sumaMat(nf,nc,matriz1,matriz2)

    #Mostrar resultados
    mostrar(matriz1,matriz2,nf,nc,suma)

    print("Bye bye")

main()