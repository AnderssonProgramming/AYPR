def pedir_datos():
    n=int(input("Ingrese el límite de números: "))
    return n

def impar(n):
    cont=0

    while cont <= n:
        cont=2*cont+1
    
    return cont

def mostrar_impar(n,cont):
    print("Los impares hasta el límite de",n,"es",cont)
    
def main():

    n=pedir_datos()
    impares=impar(n)
    mostrar_impar(n,impares)

main()