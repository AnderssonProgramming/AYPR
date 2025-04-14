# Ejercicio 1
# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
# posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su
# cubo.

# Ejercicio 2
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores),
# y posterior ordene los elementos de menor a mayor.

# Ejercicio 3
# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y
# diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para
# simplificarlo vamos a suponer que febrero tiene 28 días.

# Ejercicio 4
# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida
# valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2.

# Ejercicio 5
# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de
# la siguiente información:

# • La temperatura media de cada día

# • Los días con menos temperatura

# • Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima
# coincide con ella. si no existe ningún día se muestra un mensaje de información.

import os
import random
def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
        if os.name == "posix":
           os.system ("clear")
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
           os.system ("cls")
   
def menu():
	
	print ("Selecciona una opción")
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t4 - tercera opción")
	print ("\t9 - salir")
        


def operacion1():
    print("Hola 1")
    

def operacion2():
    print("Hola")


def main():

    #saludo()
    print ("Bienvenidos al programa")
    

    while True:
        borrarPantalla()
        menu()
        
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu=="1":

            # Inicializa una lista con 10 valores aleatorios del 1 al 10
            lista = [random.randint(1, 10) for i in range(10)]

            # Itera a través de la lista y muestra cada elemento junto con su cuadrado y cubo
            for elemento in lista:
                cuadrado = elemento ** 2
                cubo = elemento ** 3
                print(f"Elemento: {elemento}, Cuadrado: {cuadrado}, Cubo: {cubo}")
            
            operacion1()

            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
            
           
        elif opcionMenu=="2":
            
            # Inicializa una lista con 10 valores aleatorios
            lista = [random.randint(1, 100) for i in range(10)]  # Cambia el rango según tus necesidades

            # Muestra la lista original
            print("Lista original:")
            print(lista)

            # Ordena la lista de menor a mayor
            lista_ordenada = sorted(lista)

            # Muestra la lista ordenada
            print("Lista ordenada de menor a mayor:")
            print(lista_ordenada)
           
            operacion2()
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")

        elif opcionMenu=="3":

            # Definir listas con los nombres de los meses y la cantidad de días en cada mes
            nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
            dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            # Pedir al usuario un número de mes (1-12)
            numero_mes = int(input("Ingresa un número de mes (1-12): "))

            # Verificar si el número de mes es válido
            if 1 <= numero_mes <= 12:
            # Obtener el nombre del mes y la cantidad de días
                nombre_mes = nombres_meses[numero_mes - 1]
                cantidad_dias = dias_meses[numero_mes - 1]

            # Mostrar la información al usuario
                print(f"{nombre_mes} tiene {cantidad_dias} días.")
            else:
                print("Número de mes no válido. Debe ser un número entre 1 y 12.")
            
           # operacion()
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        elif opcionMenu=="4":
            # Declarar tres listas
            lista1 = []
            lista2 = []
            lista3 = []

            # Pedir al usuario que ingrese valores para lista1
            print("Ingresa valores para lista1:")
            for i in range(5):
                valor = int(input(f"Ingresa el valor {i + 1}: "))
                lista1.append(valor)

                # Pedir al usuario que ingrese valores para lista2
                print("\nIngresa valores para lista2:")
            for i in range(5):
                valor = int(input(f"Ingresa el valor {i + 1}: "))
                lista2.append(valor)

            # Calcular lista3 como la suma de lista1 y lista2
            for i in range(5):
                suma = lista1[i] + lista2[i]
                lista3.append(suma)

            # Mostrar las tres listas
            print("\nlista1:", lista1)
            print("lista2:", lista2)
            print("lista3 (suma de lista1 y lista2):", lista3)
            
            input("Has pulsado la opción 4...\npulsa una tecla para continuar")

        elif opcionMenu=="5":
            # Inicializar listas para las temperaturas mínimas y máximas de 5 días
            temperaturas_minimas = []
            temperaturas_maximas = []

            # Pedir al usuario que ingrese las temperaturas
            for dia in range(1, 6):
                temperatura_min = float(input(f"Ingrese la temperatura mínima del día {dia}: "))
                temperatura_max = float(input(f"Ingrese la temperatura máxima del día {dia}: "))
    
            temperaturas_minimas.append(temperatura_min)
            temperaturas_maximas.append(temperatura_max)

            # Calcular la temperatura media de cada día
            temperaturas_medias = [(min_temp + max_temp) / 2 for min_temp, max_temp in zip(temperaturas_minimas, temperaturas_maximas)]

            # Calcular la temperatura mínima
            temperatura_minima = min(temperaturas_minimas)

            # Encontrar los días con menos temperatura
            dias_menos_temperatura = [i + 1 for i, temp in enumerate(temperaturas_minimas) if temp == temperatura_minima]

            # Pedir una temperatura al usuario
            temperatura_buscada = float(input("Ingrese una temperatura máxima a buscar: "))

            # Encontrar los días con la temperatura máxima ingresada
            dias_con_temperatura_buscada = [i + 1 for i, temp in enumerate(temperaturas_maximas) if temp == temperatura_buscada]

            # Mostrar la información
            print("Temperatura media de cada día:")
            for dia, temp_media in enumerate(temperaturas_medias, start=1):
                print(f"Día {dia}: {temp_media}°C")

            print(f"Días con menos temperatura ({temperatura_minima}°C): {dias_menos_temperatura}")

            if dias_con_temperatura_buscada:
                print(f"Días con temperatura máxima de {temperatura_buscada}°C: {dias_con_temperatura_buscada}")
            else:
                print("No hay días con la temperatura máxima ingresada.")

            input("Has pulsado la opción 5...\npulsa una tecla para continuar")
            
            
        elif opcionMenu=="9":
            print("Chao Chao")
            break

        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    print("Hola mundo hasta luego")
main()
