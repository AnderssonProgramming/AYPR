"""PROGRAMA <CORRECCIÓN PRIMER PARCIAL AYPR>
================================================================

ASIGNATURA : Algoritmos y programación de computadores
OBJETIVO : Este parcial consiste en hacer dos programas en donde:

           1) La empresa “Unica” quiere saber cuánta plata debe reservar para los regalos 
           de los empleados y sus hijos en la próxima Navidad.

           2) Dados n puntos de una función (x,f(x)),hallar sus valores máximos y mínimos y en
           qué valores de x ocurren. También debe decir a qué intervalo del dominio corresponden 
           los puntos dados.

AUTOR(ES) : Andersson David Sánchez Méndez
FECHA: 19/09/23
"""


def main():

    #Primer punto primera manera

    #Bienvenida
    print("Bienvenido")
    print("Este primer punto consiste en mostrar cuánta plata debe reservar la empresa Unica para los regalos de los empleados y sus hijos respecto a su edad en la próxima Navidad")

    #Entrada de datos

    e=int(input("Ingrese el número de empleados: "))
    dineronohijos=0
    dineroH_0_8=0
    dineroH_9_12=0

    contE=1 #Contador de empleados

    #Proceso

    while contE <= e:
        print("Empleado",contE)
        si_no=input("Señor empleado, usted tiene hijos?: ")

        if si_no=="SI" or si_no=="Si" or si_no=="si":

            edad0_8=int(input("Ingrese cuántos hijos tiene que esté en el intervalo de 0 a 8 años: "))
            edad9_12=int(input("Ingrese cuántos hijos tiene que esté en el intervalo de 9 a 12 años: "))

            dineroH_0_8=dineroH_0_8+edad0_8*80000
            dineroH_9_12=dineroH_9_12+edad9_12*50000

        else: 
            dineronohijos=dineronohijos+200000   

        contE=contE+1

    totaldinero=dineronohijos+dineroH_0_8+dineroH_9_12

    #Impresión de datos

    print("El total de reserva de regalos es de: ",totaldinero)
    print("La reserva de regalos para los empleados que no tienen hijos es de: ",dineronohijos)
    print("La reserva de regalo para hijos entre 0 y 8 años es de: ",dineroH_0_8)
    print("La reserva de regalos para hijos entre 9 y 12 años es de: ",dineroH_9_12)

    #Despedida

    print("Adiós")

main()


def main():

    #Primer punto segunda manera

    #Bienvenida
    print("Bienvenido")
    print("Este primer punto consiste en mostrar cuánta plata debe reservar la empresa Unica para los regalos de los empleados y sus hijos respecto a su edad en la próxima Navidad")

    #Entrada de datos

    e=int(input("Ingrese la cantidad de empleados: "))
    
    dineronohijos=0
    dineroH_0_8=0
    dineroH_9_12=0

    contE=1 #Contador empleados

    #Proceso

    while contE <= e:
        print("Empleado",contE)
        cantidadHijos=int(input("Ingrese la cantidad de hijos que tiene: "))
        
        if cantidadHijos==0:
            dineronohijos=dineronohijos+200000

        else: 
            contHijos=1 #Contador hijos para después preguntar la edad a cada hijo

            while contHijos <=cantidadHijos:
                edadHijo=int(input("Ingrese la edad de su hijo: "))

                if edadHijo>0 and edadHijo<=8:
                    dineroH_0_8=dineroH_0_8+80000

                else: 
                    if edadHijo>8 and edadHijo<=12:
                        dineroH_9_12=dineroH_9_12+50000

                contHijos=contHijos+1
        
        contE=contE+1
    
    totaldinero=dineronohijos+dineroH_0_8+dineroH_9_12
    
    #Impresión de datos

    print("El total de reserva de regalos es de: ",totaldinero)
    print("La reserva de regalos para los empleados que no tienen hijos es de: ",dineronohijos)
    print("La reserva de regalo para hijos entre 0 y 8 años es de: ",dineroH_0_8)
    print("La reserva de regalos para hijos entre 9 y 12 años es de: ",dineroH_9_12)

    #Despedida

    print("Chao chao")

main()


    #Segundo punto

def main():

    #Bienvenida
    print("Bienvenido")
    print("El segundo punto consiste en mostrar cuál es el valor máximo y mínimo respecto a n términos de parejas ordenadas, identificando el valor de x. Además, muestra  el dominio al que pertenece")

    #Entrada de datos

    n=int(input("Ingrese el número de términos: "))

    cont=2

    x=float(input("Ingrese la abscisa (valor de x): "))
    y=float(input("Ingrese la ordenada (valor de y): "))

    dominioXmax=x
    dominioXmin=x

    ymax=y
    ymin=y

    x_ocurremax=x
    x_ocurremin=x

    #Proceso

    while cont <= n:
        print("Coordenada",cont)
        x=float(input("Ingrese la abscisa (valor de x): "))
        y=float(input("Ingrese la ordenada (valor de y): "))

        if y>ymax:
            ymax=y
            x_ocurremax=x
        
        if y<ymin:
            ymin=y
            x_ocurremin=x
        
        if x>dominioXmax:
            dominioXmax=x
        
        if x<dominioXmin:
            dominioXmin=x
        
        cont=cont+1
    
    #Impresión de datos

    print("El máximo de",n,"términos es y= ",ymax, "y ocurre en x=",x_ocurremax)
    print("El mínimo de",n,"términos es y= ",ymin, "y ocurre en x=",x_ocurremin)
    print("El dominio en el que ocurre es [",dominioXmin,",",dominioXmax,"]")

    #Despedida
    print("Bye bye")
    
    
main()