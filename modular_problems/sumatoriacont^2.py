def pedir_datos():
    n=int(input("Digite cualquier número entero: "))
    return n

def sumatoria(n):
    cont=1
    suma=0

    while cont <= n:
        suma=suma+cont**2
        cont=cont+1
    return suma

def mostrar_datos(n,suma):
    print("El resultado de la sumatoria es: ",suma,"con n=",n)

def main():
    n=pedir_datos()
    suma=sumatoria(n)
    mostrar_datos(n,suma)
    
main()