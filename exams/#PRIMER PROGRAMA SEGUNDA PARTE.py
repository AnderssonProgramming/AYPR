#PRIMER PROGRAMA SEGUNDA PARTE
def pedir_datos():
    n = int(input("Digite la cantidad de términos: "))
    return n

def fibonacci_recursivo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def main():
    n = pedir_datos()
    
    # Mostrar la Sucesión (f(n+1))/f(n):")
    print("Sucesión:")
    for i in range(1, n):
        resultado = fibonacci_recursivo(i+1) / fibonacci_recursivo(i)
        print(resultado, end=" ")

main()

