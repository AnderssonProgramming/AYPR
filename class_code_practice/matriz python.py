MAXFI=20
MAXCOL=20
def pedir_tam(dato):
    tam=-1
    if dato =="filas":
        while tam <=0 or tam > MAXFI:
            tam=int(input("Digite el tamaño: "))
    else: 
        while tam <=0 or tam > MAXCOL:
            tam=int(input("Digite el tamaño: "))
    
    return tam

def crear_inicializar():
    matriz=[[0 for nf in range(MAXFI)]for nc in range (MAXCOL)]

    return matriz

def llenarMatriz(nf,nc,matriz):

    for f in range (0,nf):
        for c in range (0,nc):
            print("(", f , ",", c , ") =", end= "")
            matriz [f][c]=int(input ())

def comparacion(nf,nc,matriz):

    # for f in range (0,nf):
    #     for c in range (0,nc):
    #         if matriz[f][c] != matriz [c][f]:

    #             no=1
    
    # return no

    encontro=0
    f=0
    while f < nf and encontro==0:
        c=0
        while c < nc:
            if matriz [f][c]!=matriz [c][f]:
                encontro=1
            
            c=c+1
        f=f+1
    
    return encontro
    

def mostrar(matriz,nf,nc,encontro):

    print("\n\n"," R E SU L T A D O S".center(60, ":"))
    print("\nMatriz:")

    #Muestro la matriz

    mostrarMat(matriz,nf,nc)

    if encontro==1:
        print("La matriz no es simétrica")
    
    else: 
        print("La matriz es simétrica")

def mostrarMat(matriz,nf,nc):
    for f in range (0,nf):
        for c in range (0,nc):
            print(format (matriz[f][c],"3d"),end= " ")
        
        print("\n", end = " ")

def main():
    print("Bienvenido")
    #Pedir tamaño de las matrices
    print("Digite una matriz cuadrada")
    print("Número de filas de su matriz")

    nf=pedir_tam("filas")
    print("Número de columnas de su matriz")
    nc=pedir_tam("columnas")

    matriz=crear_inicializar()
    #Llenar la matriz
    llenarMatriz(nf,nc,matriz)

    #Comparación
    comparacion(nf,nc,matriz)
    #Mostrar matriz
    mostrar(nf,nc,matriz)

    print("Bye bye")

main()
