"""PROGRAMA <Segundo parcial grupo 65>
================================================================

ASIGNATURA : AYPR -65
OBJETIVO : Hacer un programa modular que desarrolle el segundo parcial
AUTOR(ES) : Andersson David Sánchez Méndez
FECHA: 25/10/2023
"""
"CORRECCIÓN"

#PRIMER PUNTO

MAXV = 20

# def pide_tamaño():
#     tam = -1
#     while tam <= 0 or tam >= MAXV:
#         tam = int(input("Digite el límite del vector: "))
#     return tam

def pedir_datos():
    numero= -1
    while numero <= 0:
        numero = int(input(" Digite el número decimal que se va mostrar como número binario: "))
    return numero

def crear_vector():
    vector = [-3 for i in range(0, MAXV)]
    return vector

def decimal_binario(numero):
    if numero <= 0:
        return "0"
    
    binario = ""

    while numero > 0:
        residuo = int(numero % 2)
        decimal = int(numero / 2)
        binario = str (residuo)+ binario
        numero = decimal

    return binario

def mostrar_vector( vector, binario,numero):
    for pos in range(0, 1):
        vector[pos] = str(binario)
        print("El número decimal",numero,"a número binario es:", vector[pos], end=" ")

def main():
    print("Bienvenido")
    print("Este programa convertirá un número decimal a binario")
    # tam = pide_tamaño()
    numero = pedir_datos()
    vector = crear_vector()
    binario = decimal_binario(numero)
    mostrar_vector( vector, binario,numero)

    print("\nBye bye")

main()

#SEGUNDO PUNTO

MAXF=20
MAXC=20

def pedir_tam(cual):
    tam=-1

    if cual=="filas":
        while tam<=0 or tam>MAXF:
            tam=int(input("digite el tamaño"))
    else:
        while tam<=0 or tam>MAXF:
            tam=int(input("digite el tamaño"))

    return tam

def crear_inicia_matriz():
    matriz=[[0 for nf in range (MAXF)]for nc in range(MAXC)]

    return matriz

    
def llenarMatriz(nf,nc,matriz):
    
    for f in range (0,nf):
        for c in range (0,nc):
            print ("(", f, ",", c, ") =", end = " ")
            matriz[f][c] = int (input ( ))

def totalPersonas_columna1(nc,matrizCinema):
    resultadoT= 0
    for i in range(1,nc):
        resultadoT = resultadoT + matrizCinema[0][i]
    return resultadoT

def total_personasCine(nf,nc,matrizCinema):
    resultadoT = 0
    for f in range (0,nf):
        for c in range (1,nc):
            resultadoT = resultadoT + matrizCinema[f][c]
    return resultadoT

def ciudad_sala_mayor(nf,nc,matrizCinema):
    j = 0
    i=0
    ciudadmayor = 0

    for f in range (0,nf):
        total_ciudad = 0
        total_ciudadMayor = 0
        filaCiudadMayor = 0

        for c in range (1,nc):
            total_ciudad = total_ciudad + matrizCinema[f][c]

        if  total_ciudad > total_ciudadMayor:
            total_ciudadMayor = total_ciudad
            filaCiudadMayor = f    

        for c in range(1,nc):
            mayor = matrizCinema[0][0]

            if matrizCinema[filaCiudadMayor][c] > mayor:
                
                ciudadmayor = c

    

    return [matrizCinema[filaCiudadMayor][0],ciudadmayor]

def mostrar_datos(t_p_c_1,t_p_c,ciudadMayor,salaMayor):
    print("En la ciudad 1 ingresaron ",t_p_c_1)
    print("Total de personas que asistieron a cine: ",t_p_c)
    print("La sala de cine y la ciudad en la que más personas ingresaron a cine fue: Ciudad:",ciudadMayor," Sala ",salaMayor)
    
def mostrarMat (matriz, nf, nc):
    for f in range (0, nf):
        for c in range (0, nc):
            print (format (matriz[f][c], "5d"), end = " ")
        print ("\n", end = "")

def main():

    print("Bienvenidos")
    
    #Pedir tamaños de las matrices
    print("Numero de filas de su matriz")

    nf=pedir_tam("filas")

    print("Numero de columnas de su matriz")

    nc=pedir_tam("columnas")

    matrizCinema = crear_inicia_matriz()

    llenarMatriz(nf,nc,matrizCinema)

    #TOTAL DE PERSONAS EN LA CIUDAD 1

    t_p_c_1 = totalPersonas_columna1(nc,matrizCinema)

    #TOTAL DE PERSONAS QUE INGRESARON A CINE

    t_p_c = total_personasCine(nf,nc,matrizCinema)

    #LA CIUDAD Y SALA CON MÁS PERSONAS

    [ciudadMayor,salaMayor] = ciudad_sala_mayor(nf,nc,matrizCinema)

    #MOSTRAR RESULTADOS

    print ("\n\n", "R e s u l t a d o s Punto 2".center(60, ":"))

    mostrar_datos(t_p_c_1,t_p_c,ciudadMayor,salaMayor)

    print("Chao chao")

main()
