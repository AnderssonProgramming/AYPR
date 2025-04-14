def pedir_datos():
    n=-1
    m=-1

    while n<0:
        n=int(input("Ingrese un número entero: "))

    while m < 0:
        m=int(input("Ingrese otro número que sea menor que el número anterior: "))
    
    return[n,m]

def factorial (num):
    cont=1
    fact=1

    while cont <= num:
        fact=fact*cont
        cont=cont+1
    
    return fact

def mostrar_datos(n,m,término):
    print("La combinatoria es: ",término,"con n=",n,"y m=",m)

def main():
    [n,m]=pedir_datos()
    fact1=factorial(n)
    fact2=factorial(m)
    resta=n-m
    fact3=factorial(resta)

    término=fact1/(fact2*fact3)
    mostrar_datos(n,m,término)

main()