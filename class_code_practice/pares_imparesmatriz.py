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

def par_impar(nf,nc,matriz):
    par=0
    impar=0

    for f in range (0,nf):
        for c in range (0,nc):
            if matriz[f][c]%2==0:
                par=par+1
            
            else:
                impar=impar+1
    
    return [par,impar]


    

def mostrar (matriz,nf,nc,par,impar):
    print("\n\n", " R e s u l t a d o s ".center(60, ":"))
    print("\nMatriz: ")

    #Muestro la matriz
    mostrarMat(matriz,nf,nc)

    #Muestro la suma
    print("\n La cantidad de elelmentos pares es: ",par)
    print("\n La cantidad de elementos impares es: ",impar)

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
    contpar_impar=par_impar(nf,nc,matriz)

    #Mostrar resultados
    mostrar(matriz,nf,nc,contpar_impar)

    print("Bye bye")

main()