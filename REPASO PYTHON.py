#PRIMER PROGRAMA

def pedir_lado():

    lado=int(input("Digite la medida del lado del cuadrado en cm: "))

    return lado

def superficieCuadrado(lado):

    superficie=lado**2

    return superficie

def mostrar_datos(lado,superficie):
    print("El cuadrado con longitud de sus lados de",lado,"cm, tiene una superficie de: ",superficie,"cm^2")

def main():
    n=pedir_lado()
    superficie=superficieCuadrado(n)
    mostrar_datos(n,superficie)

main()

#SEGUNDO PROGRAMA

def pedir_numeros():
    n1=-1
    n2=-1
    while n1 <=0 and n2 <=0:
        n1=int(input("Digite el primer número entero: "))
        n2=int(input("Digite el segundo número entero: "))
    
    return [n1,n2]

def sumaNum(n1,n2):
    suma=n1+n2
    return suma

def productoNum(n1,n2):
    producto=n1*n2
    return producto

def mostrar_datos(n1,n2,suma,producto):
    print("Dado los números,",n1,"y",n2, ",la suma y producto de estos números respectivamente es: ",suma, "y",producto)

def main():
    [n1,n2]=pedir_numeros()
    suma=sumaNum(n1,n2)
    producto=productoNum(n1,n2)
    mostrar_datos(n1,n2,suma,producto)

main()

#TERCER PROGRAMA

def pedir_numeros():
    n1=-1
    n2=-1
    n3=-1
    n4=-1
    while n1 <=0 and n2 <=0 and n3<=0 and n4<=0:
        n1=int(input("Digite el primer número entero: "))
        n2=int(input("Digite el segundo número entero: "))
        n3=int(input("Digite el tercer número entero: "))
        n4=int(input("Digite el cuarto número entero: "))
    
    return [n1,n2,n3,n4]

def sumaNum(n1,n2):
    suma=n1+n2
    return suma

def productoNum(n3,n4):
    producto=n3*n4
    return producto

def mostrar_datos(n1,n2,n3,n4,suma,producto):
    print("Dado los números,",n1,"y",n2, ",la suma de esos números es",suma,"y dado los números,",n3,"y",n4,", el producto de estos números es ",producto)

def main():
    [n1,n2,n3,n4]=pedir_numeros()
    suma=sumaNum(n1,n2)
    producto=productoNum(n3,n4)
    mostrar_datos(n1,n2,n3,n4,suma,producto)

main()

#CUARTO PROGRAMA

def main():
    n=-1
    while n <=0:
        n=int(input("Digite la cantidad de números que desea: "))

    suma=0
    for i in range (0,n):
        print("Número",i)
        num=int(input("Digite el número: "))
        suma=suma+num

    promedio=suma/n

    print("El promedio de ",n,"números es: ",promedio,"con suma de ",suma)

main()

#QUINTO PROGRAMA

def main():

    sueldoPersona=int(input("Ingrese su sueldo: "))

    if sueldoPersona > 3000:
        print("Debe abonar impuestos")
    
    # else:
    #     print("No debe abonar impuestos")
    
main()

#SEXTO PROGRAMA

def main():
    n1=-1
    n2=-1

    while n1<=0 and n2<=0:
        n1=int(input("Digite un número: "))
        n2=int(input("Digite otro número distinto: "))
    
    if n1 > n2:
        print("El número mayor es: ",n1)
    
    else:
        print("El número mayor es: ",n2)

main()

#SÉPTIMO PROGRAMA

def main():
    num=float(input("Digite un número: "))

    if num !=0:
        numero=num*10
    
    else:
        num=float(input("Digite otro número distinto de cero: "))
        numero=num*10
    
    print("El número",num,"multiplicado por 10 es: ",numero)

main()

#OCTAVO PROGRAMA

def main():
    n1=-1
    n2=-1

    while n1<=0 and n2<=0:
        n1=int(input("Digite un número: "))
        n2=int(input("Digite otro número: "))

    if n1==n2:
        print("PELIGRO, los dos números son iguales")
        print("Ingrese dos números DIFERENTES ")
        n1=int(input("Digite un número: "))
        n2=int(input("Digite otro número: "))

    else:
        print("PROCESS")
        

main()

#NOVENO PROGRAMA

def main():
    n1=-1
    n2=-1

    while n1<=0 and n2<=0:
        n1=int(input("Digite un número: "))
        n2=int(input("Digite otro número: "))

    if n1 > n2:
        suma= n1+n2
        diferencia= n1-n2
        print("La suma y diferencia de los números,",n1,"y",n2,"respectivamente es: ",suma,",",diferencia)
    else:
        producto= n2*n1
        división=n2/n1
        print("El producto y división de los números,",n1,"y",n2,"respectivamente es: ",producto,",",división)
    
main()

#DÉCIMO PROGRAMA

def main():
    n=-1
    while n <=0:
        n=int(input("Digite la cantidad de notas que desea: "))

    suma=0
    for i in range (0,n):
        print("Nota",i)
        num=int(input("Digite el número: "))
        suma=suma+num

    promedio=suma/n 
    if promedio >=7:
        print("PROMOCIONADO: El promedio de ",n,"notas es: ",promedio)
    
    else:
        print("REPROBADO: El promedio de ",n,"notas es: ",promedio)

main()

#UNDÉCIMO PROGRAMA
def pedir_numero():
    n=-1
    while n<=0:
        n=int(input("Ingrese un número de 1 o 2 dígitos: "))
    
    return n

def dosDigitosNum(n):
    if n // 10 >=1:
        print("El número",n, "tiene dos dígitos")
    
    else:
        print("El número",n, "tiene un sólo dígito")


def main():
    n=pedir_numero()
    dosDigitosNum(n)

main()

#DOCE PROGRAMA

def main():
    n=-1
    while n <=0:
        n=int(input("Digite la cantidad de notas que desea: "))

    suma=0
    for i in range (0,n):
        print("Nota",i)
        num=int(input("Digite el número: "))
        suma=suma+num

    promedio=suma/n 
    if promedio >=7:
        print("PROMOCIONADO: El promedio de ",n,"notas es: ",promedio)
    
    elif promedio >=4 and promedio < 7:
        print("REGULAR: El promedio de ",n,"notas es: ",promedio)
        
    else: 
        print("REPROBADO: El promedio de ",n,"notas es: ",promedio)

main()

#TRECE PROGRAMA

def main():
    cantidadPreg=int(input("Digite la cantidad de preguntas que se realizaron: "))
    cantidadPregCorrec=int(input("Digite la cantidad de respuestas correctas: "))

    porcentaje=cantidadPregCorrec/cantidadPreg

    if porcentaje >= 0.9:
        print("Obtuvo en su test de capacitación un nivel máximo con",porcentaje*100,"%", "de 100%")
    elif porcentaje >= 0.75 and porcentaje < 0.9:
        print("Obtuvo en su test de capacitación un nivel medio con",porcentaje*100,"%", "de 100%")
    
    elif porcentaje >= 0.5 and porcentaje < 0.75:
        print("Obtuvo en su test de capacitación un nivel regular con",porcentaje*100,"%", "de 100%")
    
    else:
        print("Obtuvo en su test de capacitación un fuera de nivel con",porcentaje*100,"%", "de 100%")

main()

#CATORCE PROGRAMA

def main():

    n=int(input("Digite la cantidad de números que desea: "))
    numMax=int(input("Digite el número base: "))

    for i in range (1,n):
        numero=int(input("Digite número: "))

        if  numero > numMax:
            numMax= numero
    
    print("El número mayor de",n,"números es: ",numMax )

main()

#QUINCE PROGRAMA

def main():
    dia=int(input("Digite el número del día: "))
    mes=int(input("Digite el número de mes: "))
    año=int(input("Digite el año: "))
    MES=""
    if mes==1:
        MES="Enero"
        print("Corresponde al primer trimestre del año con día",dia,"y mes", MES)
    else: 
        if mes==2:
            MES="Febrero"
            print("Corresponde al primer trimestre del año con día",dia,"y mes", MES)
        else: 
            if mes==3:
                MES="Marzo"
                print("Corresponde al primer trimestre del año con día",dia,"y mes", MES)
            else: 
                print("No corresponde al primer trimestre del año",año)

main()

#DIECISEIS PROGRAMA

def main():
    print("Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad")

    dia=int(input("Digite el número del día: "))
    mes=int(input("Digite el número de mes: "))
    año=int(input("Digite el año: "))

    if dia == 24 and mes== 12:
        print("La fecha ingresada corresponde a Navidad",dia,"-",mes,"-",año)
    
    else:
        print("La fecha ingresada no es Navidad :(((((((())))))))")
main()

#DIECESIETE PROGRAMA

def cantidad():

    n=-1
    while n <=0:
        n=int(input("Digite la cantidad de términos que desea: "))
    
    return n

def process(n):
    numeros=[]
    for i in range (0,n):
        print("Número",i+1)
        num=int(input("Digite número: "))
        numeros.append(num)

    return numeros

def two(numeros):

    todos_menores_diez = True
    for num in numeros:
        if num >= 10:
            todos_menores_diez = False
            break
    return todos_menores_diez


    # for i in range (0,n):
    #     print("Número",i+1)
    #     num=int(input("Digite número: "))

    #     if num < 10:
    #         print("Todos los números son menores a diez")

    #     else:
    #         print("Hay algún número que es mayor a 10")
def main():
    print("Se ingresan por teclado n números, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda. Todos los números son menores a diez")

    n=cantidad()
    proceso=process(n)
    if two(proceso):
        print("Todos los números son menores a diez")

    else:
        print("Hay algún número que es mayor a 10")

main()

#DIECIOCHO PROGRAMA

def main():
    print("Se ingresan por teclado tres números, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda. Alguno de los números es menor a diez")

    num1=float(input("Digite primer número: "))
    num2=float(input("Digite segundo número: "))
    num3=float(input("Digite tercer número: "))

    if num1 < 10 or num2 < 10 or num3 < 10:
        print("Alguno de los números es menor a diez")
    
    else: 
        print("Cómase un cerro")

main()

#DIECINUEVE PROGRAMA

def main():
    print("Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero")

    num1=float(input("Digite primer número: "))
    num2=float(input("Digite segundo número: "))
    num3=float(input("Digite tercer número: "))

    if num1==num2 and num2==num3:
        suma=num1+num2
        multiplicación=suma*num3
    
        print("La suma de los primeros dos números es",suma,"con producto de esa suma por el tercer número de: ",multiplicación)
    
    else:
        print("GET OUTTA HERE")
main()

#VEINTE PROGRAMA

def main():
    print("Escribir un programa que pida ingresar la coordenada de un punto en el plano, es decir dos valores enteros x e y (distintos a cero).Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto. (1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)")

    n=int(input("Digite la cantidad de coordenadas: "))

    for pos in range (0,n):
        x=float(input("Digite el valor de la abscisa (x): "))
        y=float(input("Digite el valor de la ordenada (y): "))

        if x > 0 and y > 0:
            print("La coordenada (",x,",",y,") pertenece al primer cuadrante")
        
        elif x <0 and y > 0:
            print("La coordenada (",x,",",y,") pertenece al segundo cuadrante")
        
        elif x < 0 and y < 0:
            print("La coordenada (",x,",",y,") pertenece al tercer cuadrante")
        
        else: 
            print("La coordenada (",x,",",y,") pertenece al cuarto cuadrante")

 
main()

#VEINTIÚN PROGRAMA

def main():
    print("De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe")
            # a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
            # b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %.
            # c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.")
    
    sueldo=float(input("Digite su sueldo: "))
    añosAntiguedad=int(input("Digite los años que lleva en la empresa: "))

    if sueldo < 500 and añosAntiguedad >= 10:
        nuevoSueldo= sueldo + sueldo * 0.20
        print("El nuevo sueldo es de: ",nuevoSueldo,"con un aumento del 20%")
    
    elif sueldo < 500 and añosAntiguedad < 10:
        nuevoSueldo= sueldo + sueldo * 0.05
        print("El nuevo sueldo es de: ",nuevoSueldo,"con un aumento del 5%")
    
    else:
        print("Su saldo se mantiene igual: ",sueldo)


main()

#VEINTIDOS PROGRAMA

def main():
    print("Escribir un programa en el cual: dada una lista de n valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)")

    n=int(input("Digite la cantidad de números que desea: "))

    x=float(input("Digite número base: "))
    max=x
    min=x

    for j in range (1,n):
        x=float(input("Digite número: "))

        if x > max:
            max=x
            
        if x < min:
            min=x
            

    print("El número mayor es: ",max)
    print("El número menor es: ",min)
    
main()

#VEINTITRES PROGRAMA

def main():
    print("Realizar un programa que imprima en pantalla los números del 1 al 100.")

    cont=0

    while cont < 100:
        cont+=1
        print(cont,end=" ")
main()

#VEINTICUATRO PROGRAMA

def main():

    print("\n","Imprimir los números del 1 al 500")
    x=1

    while x <=500:
        print(x, end=" ")
        x+=1

main()

def main():

    print("\n","Imprimir los números del 50 al 100")
    x=50

    while x<=100:
        print(x,end=" ")
        x+=1

main()

def main():

    print("\n","Imprimir los números del -50 al 0")
    x=-50

    while x <=0:
        print(x,end=" ")
        x+=1
        
main()

def main():

    print("\n","Imprimir los números del 2 al 100 pero de 2 en 2 (2,4,6,8 ....100")
    x=2

    while x %2==0 and x <=100:
        print(x,end=" ")
        x+=1
    
        if x %2!=0:
            x+=1

main()

#VEINTICINCO PROGRAMA

def main():
    print("\n","Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el valor ingresado de uno en uno")
    
    n=-1
    while n <=0:
        n=int(input("Digite un número positivo: "))
    
    x=1

    while x <= n:
        print(x,end=" ")
        x+=1

main()

#VEINTISEIS PROGRAMA

def main():
    print("\n","Desarrollar un programa que permita la carga de 10 valores por teclado y nos muestre posteriormente la suma de los valores ingresados y su promedio")

    x=1
    suma=0
    while x <=10:
        print("Número ",x)
        valor=int(input("Digite número: "))
        suma+=valor
        x+=1
    promedio=suma/10

    print("La suma de todos los valores es ",suma,"con promedio de ",promedio)

main()

#VEINTISIETE PROGRAMA

def main():
    print("Una planta que fabrica perfiles de hierro posee un lote de n piezas")
    # Confeccionar un programa que pida ingresar por teclado la cantidad de piezas a procesar y luego ingrese la longitud de cada perfil;     
    # sabiendo que la pieza cuya longitud esté comprendida en el rango de 1.20 y 1.30 son aptas. Imprimir por pantalla la cantidad de piezas aptas que hay en el lote.")

    cantidadPiezas=int(input("Ingrese la cantidad de piezas: "))

    x=1
    contPIEZAS=0

    while x <= cantidadPiezas:

        print("Pieza #",x)
        longitudPerfil=float(input("Ingrese la longitud del perfil: "))
        

        if longitudPerfil > 1.20 and longitudPerfil < 1.30:
            contPIEZAS+=1
        
        x+=1
    
    print("La cantidad de piezas aptas para la planta que fabrica perfiles de hierro es: ",contPIEZAS)

        
main()

#VEINTIOCHO PROGRAMA

def main():
    print("Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores")

    e=1

    contM=0
    contm=0

    while e <= 10:
        print("Nota",e)
        notaAlumno=float(input("Digite la nota de cada alumno: "))

        if notaAlumno >=7:
            contM+=1
        
        else:
            contm+=1

        e+=1
    
    print(contM,"estudiantes tienen notas mayores o iguales a 7")
    print(contm,"estudiantes tienen notas menores a 7")


main()

#VEINTINUEVE PROGRAMA

def main():
    print("Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas")

    cont=1
    personas=int(input ("Ingrese el número de personas: "))

    sumaAltura=0
    while cont <= personas:

        print("Persona",cont)

        altura=float(input("Digite su altura: "))
        sumaAltura+=altura
        cont+=1
    
    promedio=sumaAltura/personas

    print("La alturas promedio de las personas es de: ",promedio)

main()

#TREINTA PROGRAMA

def main():

    print("Empresa con n empleados cuyos sueldos oscilan entre $100 y $500")
    # realizar un programa que lea los sueldos que cobra cada empleado e informe 
    # cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300. 
    # Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

    cont=1
    contE_100_300=0
    contE300_=0
    sumaSueldos=0

    empleados=int(input ("Ingrese el número de empleados: "))

    while cont <= empleados:

        print("Empleado",cont)

        sueldo=float(input("Digite su sueldo: "))
        sumaSueldos+=sueldo

        if sueldo >= 100 and sueldo <= 300:
            contE_100_300+=1

        elif sueldo > 300:
            contE300_+=1

        cont+=1

    print("El número de empleados que cobran entre $100 y $300 es: ",contE_100_300)
    print("El número de empleados que cobran más de $300 es: ",contE300_)
    print("El importe total que gasta la empresa en sueldos al personal es $",sumaSueldos)
    
main()

#TREINTIÚN PROGRAMA

def main():
    print("Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)")

    cont=11

    while cont <= 11*25:
        print(cont,end=" ")

        cont+=11
main()

#TREINTAYDOS PROGRAMA

def main():
    print("\n","Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc")


    cont=8

    while cont <= 500:
        print(cont, end=" ")
        cont+=8

main()

#TREINTAYTRES PROGRAMA

"""FIRST WAY"""

def main():

    print("Realizar un programa que permita cargar dos listas de 15 valores cada una") 
        #   Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor 
        #   (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")")
    
    print("LISTA 1")
    cont=1
    sumaN=0
    while cont <= 15:

        num=float(input("Digite cualquier número: "))
        sumaN+=num

        cont+=1

    
    print("LISTA 2")
    cont=1
    sumaNum=0
    while cont <= 15:

        numero=float(input("Digite cualquier número: "))
        sumaNum+=numero

        cont+=1

    
    if sumaN > sumaNum:
        print("Lista 1 mayor con suma de sus números ",sumaN)
    
    else:
        if sumaN < sumaNum:
            print("Lista 2 mayor con suma de sus números ",sumaNum)
        
        else:
            print("Lista 1 y 2 iguales con suma de números ",sumaNum)

main()

"""SECOND WAY"""

def pedir_dato():

    n=-1

    while n <= 0:
        n=int(input("Digite la longitud de la lista: "))

        return n

def sumaListas(n):

    print("LISTA 1")

    lista1=[]
    suma1=0
    

    for pos in range (0,n):
        print("Número",pos+1)
        num=float(input("Digite número: "))

        lista1.append(num)
        suma1+=num
    
    print("LISTA 2")
    lista2=[]
    suma2=0

    for i in range (0,n):
        print("Número",i+1)
        num=float(input("Digite número: "))

        lista2.append(num)
        suma2+=num

    return [lista1,lista2,suma1,suma2]

def mostrar_datos(lista1,lista2,suma1,suma2,n):
    print("Con longitud de la lista de ",n)
    print("Lista1",lista1,end=" ")
    print("\n","Lista2",lista2,end=" ")

    print("\n","...........................................")
    if suma1 > suma2:
        print("\n","Lista 1",lista1,"mayor con la suma de sus números de",suma1)

    elif suma1 < suma2:
        print("\n","Lista 2",lista2,"mayor con suma de sus números de ",suma2)
    
    else:
        print("\n","Lista 1 y lista 2 iguales con suma de sus números ",suma1)

def main():

    n=pedir_dato()

    [lista1,lista2,suma1,suma2]=sumaListas(n)

    mostrar_datos (lista1,lista2,suma1,suma2,n)

main()

#TREINTAYCUATRO PROGRAMA

def main():
    print("Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares")
    # Emplear el operador “%” en la condición de la estructura condicional (este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):")

    n=int(input("Digite la cantidad de números: "))

    cont=1
    contP=0
    contI=0

    while cont <= n:
        print("Número",cont)
        num=int(input("Digite cada número: "))

        if num % 2 == 0:
            contP+=1
        
        else:
            contI+=1

        cont+=1
    
    print("Hay ",contP," números pares")
    print("Hay",contI," números impares")

main()

#TREINTAYCINCO PROGRAMA

def main():
    print("Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo") 
        #   El programa deberá informar:
        #     a) De cada triángulo la medida de su base, su altura y su superficie.
        #     b) La cantidad de triángulos cuya superficie es mayor a 12.")
    
    n=int(input("Digite la cantidad de pares de datos: "))
    cantidadT=0

    for i in range (n):

        print("Triángulo",i+1)
        medidaBase=float(input("Digite la medida de la base del triángulo: "))
        medidaAltura=float(input("Digite la medida de la altura del triángulo: "))
        superficie=(medidaBase*medidaAltura)/2
        print("La superficie del triángulo con base",medidaBase,"y altura",medidaAltura,"es de:",superficie)

        if superficie > 12:
            cantidadT+=1
        
    print("La cantidad de triángulos cuya superficie es mayor a 12 es: ",cantidadT)

main()

#TREINTAYSEIS PROGRAMA

def main():
    print("Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.")

    suma=0
    for pos in range (10):
        num=float(input("Digite número: "))

        if pos >=5:
            suma+=num
    
    print("La suma de los últimos 5 valores ingresados es: ",suma)

main()

#TREINTAYSIETE PROGRAMA

def main():
    print("Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)")

    tablaMultiplicar5=5

    for i in range (10):
        print (tablaMultiplicar5,end=" ")
        tablaMultiplicar5+=5

main()

#TREINTAYOCHO PROGRAMA

def main():
    print("Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la tabla de multiplicar del mismo (los primeros 12 términos)")
    # Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36. ")
     
    num=int(input("Digite un valor del 1 al 10: "))

    for i in range (1,13):
        tabla=num*i
        print(tabla,end=" ")
main()

#TREINTAYNUEVE PROGRAMA

def main():
    print("Realizar un programa que lea los lados de n triángulos, e informar:")
    # a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
    # b) Cantidad de triángulos de cada tipo.")

    cantidadT=int(input("Ingrese la cantidad de triángulos que quiere: "))

    cantidadT_eq=0
    cantidadT_is=0
    cantidadT_es=0

    for i in range (cantidadT):

        print("Triángulo",i+1)

        lado1=int(input("Digite la medida del lado 1: "))
        lado2=int(input("Digite la medida del lado 2: "))
        lado3=int(input("Digite la medida del lado 3: "))

        if lado1==lado2 and lado2==lado3:
            print("El triángulo número",i+1,"es equilátero")
            cantidadT_eq+=1

        elif lado1!=lado2 and lado2!=lado3:
            print("El triángulo número",i+1,"es escaleno")
            cantidadT_es+=1
        
        elif lado1+lado2 < lado3 or lado1+lado3 < lado2 or lado2+lado3 < lado1:
            print("No existe triángulo con esas medidas")

        else:
            print(("El triángulo número",i+1,"es isósceles"))
            cantidadT_is+=1
        
    
    print("La cantidad de triángulos equiláteros es: ",cantidadT_eq)
    print("La cantidad de triángulos isósceles es: ",cantidadT_is)
    print("La cantidad de triángulos escalenos es: ",cantidadT_es)

main()

#CUARENTA PROGRAMA

def main():
    print("Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.")
    # Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.")

    cantidadPuntos=int(input("Digite la cantidad de puntos a procesar: "))

    primerC=0
    segundoC=0
    tercerC=0
    cuartoC=0

    for pos in range (cantidadPuntos):
        print("Coordenada",pos+1)

        x=float(input("Digite la coordenada x: "))
        y=float(input("Digite la coordenada y: "))

        if x > 0 and y > 0:
            primerC+=1
        
        elif x < 0 and y > 0:
            segundoC+=1
        
        elif x < 0 and y < 0:
            tercerC+=1
        
        else:
            cuartoC+=1
    
        print("|",x,",",y,"|")
    
    print("Cantidad de puntos primer cuadrante: ",primerC)
    print("Cantidad de punto segundo cuadrante: ",segundoC)
    print("Cantidad de puntos tercer cuadrante: ",tercerC)
    print("Cantidad de puntos cuarto cuadrante: ",cuartoC)

main()

#CUARENTAYÚN PROGRAMA

def main():
    print("Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:")
    # a) La cantidad de valores ingresados negativos.
    # b) La cantidad de valores ingresados positivos.
    # c) La cantidad de múltiplos de 15.
    # d) El valor acumulado de los números ingresados que son pares.")

    cantidadNegativos=0
    cantidadPositivos=0
    cantidadMul15=0
    sumaNumerosPares=0

    for i in range (10):
        print("Número",i+1)

        num=float(input("Digite número: "))

        if num < 0:
            cantidadNegativos+=1
        
        elif num > 0:
            cantidadPositivos+=1
        
        if num % 15 ==0:
            cantidadMul15+=1
        
        if num %2 == 0:
            sumaNumerosPares+=num
    
    print("La cantidad de valores ingresados negativos es: ",cantidadNegativos)
    print("La cantidad de valores ingresados positivos es: ",cantidadPositivos)
    print("La cantidad de múltiplos de 15 es: ",cantidadMul15)
    print("El valor acumulado de los números ingresados que son pares es: ",sumaNumerosPares)

main()

#CUARENTAYDOS PROGRAMA

def main():
    print(" Se cuenta con la siguiente información: ")
    # Las edades de 5 estudiantes del turno mañana.
    # Las edades de 6 estudiantes del turno tarde.
    # Las edades de 11 estudiantes del turno noche.
    # Las edades de cada estudiante deben ingresarse por teclado.

    # a) Obtener el promedio de las edades de cada turno (tres promedios)
    # b) Imprimir dichos promedios (promedio de cada turno)
    # c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.")

    sumaPromedioMañana=0

    for pos in range (5):
        print("Estudiante",pos+1)
        edad=int(input("Digite la edad"))
        sumaPromedioMañana+=edad
    
    sumaPromedioTarde=0

    for pos in range (6):
        print("Estudiante",pos+1)
        edad=int(input("Digite la edad"))
        sumaPromedioTarde+=edad

    sumaPromedioNoche=0

    for pos in range (11):
        print("Estudiante",pos+1)
        edad=int(input("Digite la edad"))
        sumaPromedioNoche+=edad
    
    promedioMañana=sumaPromedioMañana/5
    promedioTarde=sumaPromedioTarde/6
    promedioNoche=sumaPromedioNoche/11

    print("El promedio de edad del turno de la mañana fue de: ",promedioMañana)
    print("El promedio de edad del turno de tarde fue de: ",promedioTarde)
    print("El promedio de edad del turno de noche fue de: ",promedioNoche)

    mayor="Mañana"

    if promedioMañana > promedioTarde and promedioMañana > promedioNoche:
        mayor="Mañana"
    
    elif promedioTarde > promedioNoche:
        mayor="Tarde"
    
    else:
        mayor="Noche"
    
    print("El turno el cual tuvo un promedio de edades mayor fue: ",mayor)

main()

#CUARENTAYTRES PROGRAMA

def main():
    
    print("get outta here")
    
    nombre=input("Ingrese su nombre: ")
    nombremin=nombre.lower()

    if nombremin [0] == "j":
        print("El nombre",nombre.capitalize(),"comienza con la letra j")

    else:
        print("El nombre",nombre.capitalize()," no comienza con la letra j")

main()

#CUARENTAYCUATRO PROGRAMA

def main():
    print("Realizar la carga del nombre de una persona y luego mostrar el primer caracter del nombre y la cantidad de letras que lo componen.")

    nombrePersona=input("Digite el nombre de la persona: ")

    print("El primer carácter del nombre es: ",nombrePersona[0])

    print("La cantidad de letras que compone el nombre es: ",len(nombrePersona))
    
main()

#CUARENTAYCINCO PROGRAMA

def main():
    print("Solicitar la carga del nombre de una persona en minúsculas. Mostrar un mensaje si comienza con vocal dicho nombre")

    nombrePersona=input("Digite el nombre de la persona: ")
    nombrePersonamin=nombrePersona.lower()

    if nombrePersonamin[0]=="a" or nombrePersonamin[0]=="e" or nombrePersonamin[0]=="i" or nombrePersonamin[0]=="o" or nombrePersonamin[0]=="u":
        print("El nombre de la persona",nombrePersona,"comienza con una vocal",nombrePersonamin[0])
        
    else:
        print("El nombre no comienza con una vocal")
        
main()

#CUARENTAYSEIS PROGRAMA

def main():
    print("Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un caracter (@).")

    mail=input("Ingrese el email: ")

    cantidadCaracter=0

    for i in range (len(mail)):
        
        if mail[i]=="@":
            cantidadCaracter+=1

    if cantidadCaracter==1:
        print("El email contiene solo un carácter (@)")

    else:
        print("El email no es válido")
            
main()

#CUARENTAYSIETE PROGRAMA

def main():
    print("Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron")
    
    #Tener en cuenta que un espacio en blanco es igual a " ", en cambio una cadena vacía es ""

    oracion=input("Ingrese una oración: ")
    espacios=0
    
    for pos in range (len(oracion)):
        if oracion[pos]== " ":
            espacios+=1

    print("La cantidad de espacios en blanco que hay en la oración es: ",espacios)
    
main()

#CUARENTAYOCHO PROGRAMA

def main():
    print("Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas")
    
    #Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. Contar la cantidad de vocales.
    #Crear un segundo string con toda la oración en minúsculas para que sea más fácil disponer la condición que verifica que es una vocal

    oracion=input("Ingrese una oración que puede tener letras mayúsculas y minúsculas: ")
    oracionmin=oracion.lower()

    cantidadVocales=0

    for i in range (len(oracionmin)):
        if oracionmin[i]=="a" or oracionmin[i]=="e" or oracionmin[i]=="i" or oracionmin[i]=="o" or oracionmin[i]=="u":
            cantidadVocales+=1

    print("La cantidad de vocales de la oración es: ",cantidadVocales)
    
main()

#CUARENTAYNUEVE PROGRAMA

def main():
    print("Solicitar el ingreso de una clave por teclado y almacenarla en una cadena de caracteres.")

    #Controlar que el string ingresado tenga entre 10 y 20 caracteres para que sea válido, en caso contrario mostrar un mensaje de error.

    clave=input("Ingrese la clave que será almacenada como carácteres: ")

    longitudClave=len(clave)

    if longitudClave >=10 and longitudClave <= 20:
        print("La clave es válida")

    else:
        print("Mensaje de ERROR")
    
main()

#CINCUENTA PROGRAMA

def main():
    print("Definir una lista que almacene n enteros. Sumar todos sus elementos y mostrar dicha suma.")

    n=int(input("Ingrese la longitud de la lista: "))
    lista=[]
    suma=0

    for pos in range (n):
        num=float(input("Digite cada número: "))
        lista.append(num)
        suma+=num
    
    print("La lista: ",lista)
    print("Con suma de sus números de: ",suma)

main()

#CINCUENTAYÚN PROGRAMA

def main():
    print("Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde)")
        # Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
        # Imprimir las dos listas de sueldos.")
    
    listaMañana=[]
    listaTarde=[]

    for i in range (4):
        print("MAÑANA")
        sueldoMañana=float(input("Ingrese el sueldo: "))
        print("TARDE")
        sueldoTarde=float(input("Ingrese el sueldo: "))

        listaMañana.append(sueldoMañana)
        listaTarde.append(sueldoTarde)

    print("Lista de turno de la mañana: ",listaMañana)
    print("Lista de turno de la tarde: ",listaTarde)
    
main()

#CINCUENTAYDOS PROGRAMA

def main():
    print("Realizar un programa que pida la carga de dos listas numéricas enteras de 4 elementos cada una.")
    #   Generar una tercer lista que surja de la suma de los elementos de la misma posición de cada lista. Mostrar esta tercer lista.")

    lista1=[]
    lista2=[]

    suma=[0]
    lista3=[]

    for i in range (4):
        print("LISTA1,posición",i)

        num1=int(input("Digite cada número: "))
        lista1.append(num1)

        print("LISTA2,posición",i)

        num2=int(input("Digite cada número: "))
        lista2.append(num2)

        suma=lista1[i]+lista2[i]

        lista3.append(suma)
    
    print(lista1)
    print(lista2)
    print(lista3)


main()
