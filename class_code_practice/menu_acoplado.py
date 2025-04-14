# Claro, aquí está tu código integrado en el menú extendido:
import os

def borrarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

# 1
def lectura_procesamiento_datos():
    file = open("votacion1.txt","r")
    lista_votos = []
    for linea in file.readlines():
        # En este filtro limpiamos el espacio entre lineas de cada registro. 
        filtro_voto = linea.rstrip("\n")
        voto = filtro_voto.split(",")
        lista_votos.append(voto)
    file.close
    return lista_votos
# 2.1
def cantidad_de_votación_en_el_país(li):
    cantidad_votos = len(li)
    return cantidad_votos
# 2.2
def cantidad_de_votacion_por_ciudad(lista_votos):
    def conteo_votos_por_ciudad(c):
        numero_votos = 0
        for elemento in lista_votos:
            if elemento[2] == c:
                numero_votos = numero_votos + 1
        return numero_votos

    # creación y llenado de lista con sus respectivos votos
    lista_conteo_votos_ciudad = []
    lista_ciudades = ["Bogota", "Barranquilla", "Cali", "Medellín", "Bucaramanga", "Pasto", "Cartagena"]
    for ciudad in lista_ciudades:
        ciudad_votos = []
        numero_votos_ciudad = conteo_votos_por_ciudad(ciudad)
        ciudad_votos.append(ciudad)
        ciudad_votos.append(numero_votos_ciudad)
        lista_conteo_votos_ciudad.append(ciudad_votos)
    
    return [lista_ciudades,lista_conteo_votos_ciudad]
# 2.3
def cantidad_de_votacion_por_region(lista_conteo_votos_ciudad):
    cantidad_region_caribe = lista_conteo_votos_ciudad[1][1] + lista_conteo_votos_ciudad[6][1]
    cantidad_region_centro = lista_conteo_votos_ciudad[0][1] + lista_conteo_votos_ciudad[3][1] + lista_conteo_votos_ciudad[4][1]
    cantidad_region_sur = lista_conteo_votos_ciudad[2][1] + lista_conteo_votos_ciudad[5][1]

    return [cantidad_region_caribe,cantidad_region_centro,cantidad_region_sur]

    # ... Código de la operación 2.2
# 2.4
def votos_por_candidato_por_ciudad(lista_votos,lista_ciudades):
    lista_candidatos_por_ciudad = ["Candidato1", "Candidato2", "Candidato3", "Candidato4"]
    # función para el conteo de votos por candidato y ciudad recidos como parámetros
    def conteo_votos_por_ciudad_por_candidato(ciudad,candidato):
        votos_por_canditato = 0
        for elemento in lista_votos:
            if elemento[2] == ciudad and elemento[0] == candidato:
                votos_por_canditato = votos_por_canditato + 1
        return votos_por_canditato
    
    # Creamos la lista de forma global para poder se accedida por la funciond de conteo de votos
    lista_votos_ciudadades_candidatos = []
    #funcion que envia ciudades y candidatos a la funcion conteo de votos
    def ciudades_candidatos():
        # este contador me ayudara a llevar la traza de el indice de la ciudad en la que voy
        for ciudad in lista_ciudades:
            lista_auxiliar2 = []
            for candidato in lista_candidatos_por_ciudad:
                lista_auxiliar1 = []
                numero_votos_ciudad_candidato = conteo_votos_por_ciudad_por_candidato(ciudad,candidato)
                lista_auxiliar1.append(candidato)
                lista_auxiliar1.append(numero_votos_ciudad_candidato)
                lista_auxiliar2.append(lista_auxiliar1)
                # lista_auxiliar2.append(numero_votos_ciudad_candidato)
            lista_votos_ciudadades_candidatos.append(lista_auxiliar2)

        # print(lista_votos_ciudadades_candidatos)
    ciudades_candidatos()
    return [lista_candidatos_por_ciudad,lista_votos_ciudadades_candidatos]    
# 2.5
def ganador_por_ciudad(lista_ciudades,lista_votos_ciudadades_candidatos):
    for i in range(7):
        print("En la ciudad ",lista_ciudades[i])
        ganador = lista_votos_ciudadades_candidatos[0][0][0]
        votos_mayor = lista_votos_ciudadades_candidatos[0][0][1]
        for j in range(4):
            if votos_mayor < lista_votos_ciudadades_candidatos[i][j][1]:
                votos_mayor = lista_votos_ciudadades_candidatos[i][j][1]
                ganador = lista_votos_ciudadades_candidatos[i][j][0]
            elif votos_mayor == 0:
                ganador = "nadie"
        print("🏆El ganador fue: ",ganador)
# 2.6
def votacion_por_partido_politico(lista_partidos,lista_region_votos_ciudad):
    for partido in range(3):
        total_partido = 0
        for ciudad in range(7):
            total_partido = total_partido + lista_region_votos_ciudad[ciudad][partido]
        print("La votación por el partido politico",lista_partidos[partido],"es de: ",total_partido)
# 2.7         
def votacion_por_partido_politico_por_ciudad_y_por_region(lista_votos,lista_ciudades):
    lista_partidos = ['Partido1', 'Partido2', 'Partido3']
    lista_region_votos_ciudad= []
    for ciudad in lista_ciudades:
        p_1 = 0
        p_2 = 0
        p_3 = 0
        lista_votos_region_candidatos = []
        for voto in lista_votos:
            if voto[1] == "Partido1" and voto[2] == ciudad:
                p_1 = p_1 + 1
            elif voto[1] == "Partido2" and voto[2] == ciudad:
                p_2 = p_2 + 1
            elif voto[1] == "Partido3" and voto[2] == ciudad:
                p_3 = p_3 + 1        
        # print("En la ciudad ",ciudad,"Por partido politico el total fue:")
        # print("Por el paritdo 1:", p_1)
        # print("Por el paritdo 2:", p_2)
        # print("Por el paritdo 3:", p_3)
        lista_votos_region_candidatos.append(p_1)
        lista_votos_region_candidatos.append(p_2)
        lista_votos_region_candidatos.append(p_3)
        lista_region_votos_ciudad.append(lista_votos_region_candidatos)
    return [lista_partidos,lista_region_votos_ciudad]
# 2.8
#Pendiente ⏳
def sitio_de_las_ciudades_donde_se_presento_la_mayor_votacion(lista_votos,lista_ciudades):
    lista_sitios = ['Sitio1', 'Sitio2', 'Sitio3']
    for ciudad in lista_ciudades:
        sitio1 = 0
        sitio2 = 0
        sitio3 = 0
        lista_votos_sitios = []
        for voto in lista_votos:
            if voto[2] == ciudad and voto[3] == 'Sitio1':
                sitio1 = sitio1 + 1
            elif voto[2] == ciudad and voto[3] == 'Sitio2':
                sitio2 = sitio2 + 1
            elif voto[2] == ciudad and voto[3] == 'Sitio3':
                sitio3 = sitio3 + 1
        lista_votos_sitios.append(sitio1)
        lista_votos_sitios.append(sitio2)
        lista_votos_sitios.append(sitio3)
        indice_sitio_mayor = -2
        if lista_votos_sitios[0] == lista_votos_sitios[1] == lista_votos_sitios[2] and lista_votos_sitios[2]!= 0:
            indice_sitio_mayor = -1
        #validación no empate         
        elif lista_votos_sitios[0] == lista_votos_sitios[1] and lista_votos_sitios[2] > lista_votos_sitios[1]:
            indice_sitio_mayor = 2
        #validación no empate   
        elif lista_votos_sitios[0] == lista_votos_sitios[2] and lista_votos_sitios[1] < lista_votos_sitios[0]:
            indice_sitio_mayor = -1
        elif lista_votos_sitios[0] == lista_votos_sitios[2] and lista_votos_sitios[1] > lista_votos_sitios[0]:
            indice_sitio_mayor = 1
        #validación no empate   
        elif lista_votos_sitios[0] == lista_votos_sitios[2] and lista_votos_sitios[1] < lista_votos_sitios[0]:
            indice_sitio_mayor = -1
        elif lista_votos_sitios[1] == lista_votos_sitios[2] and lista_votos_sitios[0] > lista_votos_sitios[1]:
            indice_sitio_mayor = 0
        elif lista_votos_sitios[1] == lista_votos_sitios[2] and lista_votos_sitios[0] < lista_votos_sitios[1]:
            indice_sitio_mayor = -1
        else:
            for voto_sitio in lista_votos_sitios:
                mayor = lista_votos_sitios[0]
            if mayor < voto_sitio:
                mayor = voto_sitio
                indice_sitio_mayor = lista_votos_sitios.index(mayor)
        if indice_sitio_mayor == -2:
            print('En la ciudad ',ciudad,' no se presentaron votos')
        elif indice_sitio_mayor == -1:
            print('En la ciudad ',ciudad,"no se puede determinar dado que hay un empate entre entre dos o tres mesas")
        else:
            print('En la ciudad ',ciudad,' el sitio donde se presento la mayor votación fue: ',lista_sitios[indice_sitio_mayor])
# 2.9 
def ciudad_mayor_votacion_y_porcentaje(lista_conteo_votos_ciudad,cantidad_votos):
    mayor = lista_conteo_votos_ciudad[0][1]
    for i in range(7):
            if mayor < lista_conteo_votos_ciudad[i][1]:
                mayor = lista_conteo_votos_ciudad[i][1]
                indice_mayor = i
            # indice_sitio = lista_conteo_votos_ciudad.index(mayor)
    print('En la ciudad ',lista_conteo_votos_ciudad[indice_mayor][0],' se presentó la mayor votación y su porcentaje fue de: ', lista_conteo_votos_ciudad[indice_mayor][1]/cantidad_votos*100,'%')            
# 2.10
def en_que_region_de_colombia_se_acudio_mas_a_las_urnas(cantidad_region_caribe,cantidad_region_centro,cantidad_region_sur):
    lista_regiones = ['Caribe','Centro','Sur']
    lista_region_mas_votos = [cantidad_region_caribe,cantidad_region_centro,cantidad_region_sur]

    #Este indice nos indicara cual es la posicion de la region en la que más se acudió para ubicara en la lista de regiones
    region_indice = 0
    region_mas_votos = lista_region_mas_votos[0]
    for region_voto in lista_region_mas_votos:
        if region_mas_votos < region_voto:
            region_mas_votos = region_voto
            region_indice = lista_region_mas_votos.index(region_mas_votos)
    print("La región en donde más se acudió a las urnas fue en la region",lista_regiones[region_indice])
# 2.11
def segunda_vuelta_bogota(lista_votos):
        resultados_bogota = {}
        # Recopilar resultados de Bogotá
        for elemento in lista_votos:
            if elemento[2] == "Bogota":
                candidato = elemento[0]
                if candidato in resultados_bogota:
                    resultados_bogota[candidato] += 1
                else:
                    resultados_bogota[candidato] = 1
        
        total_votos_bogota = sum(resultados_bogota.values())
        
        # Verificar si hay votos registrados para Bogotá
        if not resultados_bogota:
            print("No hay votos registrados para la ciudad de Bogotá para poder hacer la identificación de segunda vuelta.")
            return
        
        # Obtener el candidato con más votos en Bogotá
        ganador_bogota = max(resultados_bogota, key=resultados_bogota.get)
        votos_ganador_bogota = resultados_bogota[ganador_bogota]
        
        # Calcular el porcentaje de votos del ganador en Bogotá
        porcentaje_ganador_bogota = (votos_ganador_bogota / total_votos_bogota) * 100
        
        # Verificar si hay segunda vuelta en Bogotá
        if porcentaje_ganador_bogota < 40 or (porcentaje_ganador_bogota >= 40 and porcentaje_ganador_bogota - max(resultados_bogota.values()) < 10):
            print("Se requiere segunda vuelta en Bogotá.")
            
            # Determinar los candidatos para la segunda vuelta
            candidatos_segunda_vuelta = [candidato for candidato in resultados_bogota if candidato != ganador_bogota]
            print(f"Candidatos para la segunda vuelta: {', '.join(candidatos_segunda_vuelta)}")
            
        else:
            print(f"{ganador_bogota} ha ganado en Bogotá en primera vuelta con un {porcentaje_ganador_bogota:.2f}% de los votos.")

def cantidad_de_mujeres_y_de_hombres_que_votaron(lista_votos):
    cantidad_mujeres = 0
    cantidad_hombres = 0
    for element in lista_votos:
        if element[5] == "Mujer":
            cantidad_mujeres = cantidad_mujeres + 1
        elif element[5] == "Hombre":
            cantidad_hombres = cantidad_hombres + 1
    print("Cantidad hombres: ",cantidad_hombres," y cantidad de mujeres: ",cantidad_mujeres)

def operacion_2_11():
    # ... Código de la operación 2.11
    pass

def operacion_2_12():
    # ... Código de la operación 2.12
    pass

def menu():
    print("Selecciona una opción")
    print("\t1 - Cantidad de votación en el país: ")
    print("\t2 - Cantidad de votación por ciudad: ")
    print("\t3 - Cantidad de votación por región: ")
    print("\t4 - Votos por candidato por ciudad: ")
    print("\t5 - Ganador por ciudad: ")
    print("\t6 - Votación por partido político: ")
    print("\t7 - Votación por partido político por ciudad y por región: ")
    print("\t8 - Sitio de las ciudades donde se presentó la mayor votación: ")
    print("\t9 - Qué ciudad presentó la mayor votación y su %: ")
    print("\t10 - En que región de Colombia se acudió más a las urnas: ")
    print("\t11 - Decidir si hay segunda vuelta en la ciudad de Bogotá, y quienes serían los candidatos")
    print("\t12 - Cantidad de mujeres y de hombres que votaron")
    print("\t0 - salir")

def main():
    print("Bienvenidos al programa")
    # Hacemos la lista de votos una lista global
    lista_votos = lectura_procesamiento_datos()
    #...
    cantidad_votos = cantidad_de_votación_en_el_país(lista_votos)
    # Hacemos que las listas ciudades y votos por ciudad sean globales
    [lista_ciudades,lista_conteo_votos_ciudad] = cantidad_de_votacion_por_ciudad(lista_votos)
    # Hacemos que las listas sean globales
    [lista_candidatos_por_ciudad,lista_votos_ciudadades_candidatos] = votos_por_candidato_por_ciudad(lista_votos,lista_ciudades)
    #...
    [lista_partidos,lista_region_votos_ciudad] = votacion_por_partido_politico_por_ciudad_y_por_region(lista_votos,lista_ciudades)
    #...
    [cantidad_region_caribe,cantidad_region_centro,cantidad_region_sur] = cantidad_de_votacion_por_region(lista_conteo_votos_ciudad)



    while True:
        borrarPantalla()
        menu()

        opcionMenu = input("Inserta un número valor >> ")

        if opcionMenu == "1":
            print("")
            print("Cantidad de votos en el pais fue de: ", cantidad_votos)
            input("Has pulsado la opción 1...\npulsa una tecla para continuar")

        elif opcionMenu == "2":
            print("")
            # Imprimimos los resultados
            for ciudad in lista_conteo_votos_ciudad:
                print("En la ciudad ",ciudad[0], " votaron ",ciudad[1])
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")

        elif opcionMenu == "3":
            print("")
            # operacion()
            print("En la region caribe votaron: ",cantidad_region_caribe)
            print("En la region centro votaron: ",cantidad_region_centro)
            print("En la region sur votaron: ",cantidad_region_sur)
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")

        elif opcionMenu == "4":
            print("")
            # ⭐ mostramos candidatos y sus votaciones por
            print("Los votos por ciudad por candidato fueron: ")
            for i in range(7):
                print("En la ciudad ",lista_ciudades[i])
                for j in range(4):
                        print(lista_votos_ciudadades_candidatos[i][j][0],' = ',lista_votos_ciudadades_candidatos[i][j][1])
            # operacion()
            input("Has pulsado la opción 4...\npulsa una tecla para continuar")

        elif opcionMenu == "5":
            print("")
            ganador_por_ciudad(lista_ciudades,lista_votos_ciudadades_candidatos)
            # operacion()
            input("Has pulsado la opción 5...\npulsa una tecla para continuar")

        elif opcionMenu == "6":
            print("")
            # operacion()
            votacion_por_partido_politico(lista_partidos,lista_region_votos_ciudad)
            input("Has pulsado la opción 6...\npulsa una tecla para continuar")

        elif opcionMenu == "7":
            print("")
            for ciudad in range(7):
                print("En la ciudad ",lista_ciudades[ciudad],"Por partido politico el total fue:")
                for partido in range(3):
                    print("Por el paritdo",partido+1,":", lista_region_votos_ciudad[ciudad][partido])
            # operacion()
            print("=========================== Votación por partido político por region ===========================")
            for partido in range(3):
                print(lista_partidos[partido])
                region_caribe = lista_region_votos_ciudad[1][partido] + lista_region_votos_ciudad[6][partido]
                print("En la region caribe",region_caribe)
                region_centro = lista_region_votos_ciudad[0][partido] + lista_region_votos_ciudad[3][partido] + lista_region_votos_ciudad[4][1]
                print("En la region centro",region_centro)
                region_sur = lista_region_votos_ciudad[2][partido] + lista_region_votos_ciudad[5][partido]
                print("En la region sur",region_sur)
            input("Has pulsado la opción 6...\npulsa una tecla para continuar")
        
        # Pendiente....
        elif opcionMenu == "8":
            print("")
            # operacion()
            sitio_de_las_ciudades_donde_se_presento_la_mayor_votacion(lista_votos,lista_ciudades)
            input("Has pulsado la opción 8...\npulsa una tecla para continuar")

        elif opcionMenu == "9":
            print("")
            ciudad_mayor_votacion_y_porcentaje(lista_conteo_votos_ciudad,cantidad_votos)
            # operacion()
            input("Has pulsado la opción 9...\npulsa una tecla para continuar")
            
        elif opcionMenu == "10":
            print("")
            en_que_region_de_colombia_se_acudio_mas_a_las_urnas(cantidad_region_caribe,cantidad_region_centro,cantidad_region_sur)
            input("Has pulsado la opción 10...\npulsa una tecla para continuar")

        elif opcionMenu == "11":
            print("")
            # operacion()
            segunda_vuelta_bogota(lista_votos)
            input("Has pulsado la opción 11...\npulsa una tecla para continuar")

        elif opcionMenu == "12":
            print("")
            # operacion()
            cantidad_de_mujeres_y_de_hombres_que_votaron(lista_votos)
            input("Has pulsado la opción 12...\npulsa una tecla para continuar")

        elif opcionMenu == "0":
            print("Adiós")
            break

        else:
            print("")
            input(
                "No has pulsado ninguna opción correcta...\npulsa una tecla para continuar"
            )
    print("Hasta luego")

main()

# Este código ahora tiene las funciones `operacion_2_1` hasta `operacion_2_12` que puedes llenar con el código específico de cada operación. Puedes extender o modificar estas funciones según las necesidades específicas de tus operaciones.