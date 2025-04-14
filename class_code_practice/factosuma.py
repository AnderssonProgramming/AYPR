def pedir_datos():
    h=int(input("Ingrese el valor que será operado en factorial: "))
    n=int(input("Ingrese el número de términos de la sumatoria: "))

    return [h,n]

def factorial(h):

    cont=1
    fact=1

    while cont <= h:
        fact=fact*cont
        cont=cont+1
    
    return fact
def sumatoria(n):

    suma=0
    cont=1

    while cont <= n:
        suma=suma+7+cont**2
        cont=cont+1
    
    return suma

def sumatotal (fact,suma):
    sumaTotal=fact+suma
    return sumaTotal

def mostrar_datos (h,n,sumaTotal):
    print("La suma total es: ",sumaTotal, "con h=",h," y n=",n)

    return sumaTotal
def main():
    [h,n]=pedir_datos()
    factorialL=factorial(h)
    suma=sumatoria(n)
    sumTotal=sumatotal (factorialL,suma)
    mostrar_datos(h,n,sumTotal)
main()