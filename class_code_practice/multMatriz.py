MAXFI=20
MAXCOL=20


def matriz(dato):
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

def llenarMatriz(nf1, nc1, nf2, nc2, matriz1, matriz2):
    
    for f in range(nf1):
        for c in range(nc1):
            print("(", f, ",", c, ") de la primera matriz =", end=" ")
            matriz1[f][c] = int(input())
    
    for f in range(nf2):
        for c in range(nc2):
            print("(", f, ",", c, ") de la segunda matriz =", end=" ")
            matriz2[f][c] = int(input())

def mulMat(nf, nc, matriz1, matriz2):
    multiplicacion = [[0 for nf in range(MAXFI)] for nc in range(MAXCOL)]

    for i in range(nf):
        for j in range(nc):
            for k in range(nc):
                multiplicacion[i][j] += matriz1[i][k] * matriz2[k][j]

    return multiplicacion

    
def mostrar (matriz1,matriz2,nf1,nc1,nf2,nc2,multiplicacion):
    print("\n\n", " R e s u l t a d o s ".center(60, ":"))

    print("\nMatriz 1: ")
    mostrarMat(matriz1, nf1, nc1)

    print("\nMatriz 2:")
    mostrarMat(matriz2, nf2, nc2)

    print("\n La multiplicación de las dos matrices es:")
    mostrarMat(multiplicacion, nf1, nc2)

def mostrarMat(matriz,nf,nc):
    for f in range (0,nf):
        for c in range (0,nc):
            print(format(matriz[f][c],"3d"), end= " ")
        
        print("\n", end= " ")

def main():

    print("Bienvenido")
    
    #Pedir tamaño de las matrices
    print("Número de filas de su primera matriz")

    nf1=matriz("filas")

    print("Número de columnas de su primera matriz")

    nc1=matriz("columnas")

    print("Número de filas de su segunda matriz")

    nf2=matriz("filas")

    print("Número de columnas de su segunda matriz")

    nc2=matriz("columnas")

    if nc1 != nf2:
        print("Las dimensiones de las matrices no son compatibles para la multiplicación.")

    [matriz1,matriz2]=crear_inicializar()
    #Llenar la matriz
    llenarMatriz(nf1,nc1,nf2,nc2,matriz1,matriz2)

    #Multiplicación matrices
    multiplicacion=mulMat(nf1,nc2,matriz1,matriz2)

    #Mostrar resultados
    mostrar(matriz1,matriz2,nf1,nc1,nf2,nc2,multiplicacion)

    print("Bye bye")

main()