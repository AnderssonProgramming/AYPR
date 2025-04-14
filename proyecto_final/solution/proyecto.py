import random
from collections import Counter

def leer_archivo():
    with open("votacion1.txt", 'r') as archivo:
        lineas = archivo.readlines()
    return lineas

def cantidad_votaciones_pais(lineas):
    return len(lineas)

def cantidad_votaciones_por_ciudad(lineas, ciudad):
    return sum(1 for linea in lineas if ciudad in linea)

def cantidad_votos_por_candidato_ciudad(lineas, candidato, ciudad):
    return sum(1 for linea in lineas if candidato in linea and ciudad in linea)


def determinar_region(ciudad):
    if ciudad in ["Barranquilla", "Cartagena"]:
        return "Caribe"
    elif ciudad in ["Bogotá", "Medellín", "Bucaramanga"]:
        return "Centro"
    else:
        return "Sur"

def cantidad_votaciones_por_region(lineas, region):
    return sum(1 for linea in lineas if determinar_region(linea.strip().split(',')[2]) == region)

def ganador_por_ciudad(lineas, ciudad):
    # Filtrar las líneas correspondientes a la ciudad dada
    votos_ciudad = [linea.split(',')[0] for linea in lineas if ciudad in linea]
    
    # Contar los votos de cada candidato en la ciudad
    contador_votos = Counter(votos_ciudad)
    
    # Encontrar al candidato con más votos
    ganador = contador_votos.most_common(1)[0][0]
    
    return ganador

def votacion_por_partido(lineas, partido):
    # Filtrar las líneas correspondientes al partido dado
    votos_partido = [linea.split(',')[0] for linea in lineas if partido in linea]
    
    # Contar los votos de cada candidato en el partido
    contador_votos = Counter(votos_partido)
    
    return contador_votos

def votacion_por_partido_ciudad(lineas,ciudades):
    resultados_por_ciudad = {}
    for ciudad in ciudades:
        resultados_ciudad = Counter()
        for linea in lineas:
            if ciudad in linea:
                datos = linea.strip().split(',')
                partido = datos[1]
                resultados_ciudad[partido] += 1
        resultados_por_ciudad[ciudad] = resultados_ciudad
    return resultados_por_ciudad

def votacion_por_partido_region(lineas, regiones):
    resultados_por_region = {}
    for region in regiones:
        resultados_region = Counter()
        for linea in lineas:
            ciudad = linea.strip().split(',')[2]
            if determinar_region(ciudad).lower() == region.lower():
                datos = linea.strip().split(',')
                partido = datos[1]
                resultados_region[partido] += 1
        resultados_por_region[region] = resultados_region
    return resultados_por_region

def sitio_con_mayor_votacion_por_ciudad(lineas, ciudades):
    resultados_por_ciudad_sitio = {}
    
    for ciudad in ciudades:
        resultados_ciudad_sitio = Counter()
        for linea in lineas:
            if ciudad in linea:
                datos = linea.strip().split(',')
                sitio = datos[3]
                resultados_ciudad_sitio[sitio] += 1
                
        sitio_con_mayor_votacion = resultados_ciudad_sitio.most_common(1)
        if sitio_con_mayor_votacion:
            resultados_por_ciudad_sitio[ciudad] = sitio_con_mayor_votacion[0][0]
    
    return resultados_por_ciudad_sitio

def ciudad_con_mayor_votacion(lineas, ciudades):
    resultados_ciudad = Counter()

    for ciudad in ciudades:
        votaciones_ciudad = cantidad_votaciones_por_ciudad(lineas, ciudad)
        resultados_ciudad[ciudad] = votaciones_ciudad

    ciudad_mayor_votacion, votos_mayor_votacion = resultados_ciudad.most_common(1)[0]

    porcentaje_mayor_votacion = (votos_mayor_votacion / len(lineas)) * 100

    return ciudad_mayor_votacion, porcentaje_mayor_votacion

def region_con_mayor_participacion(lineas, regiones):
    resultados_region = Counter()

    for region in regiones:
        votaciones_region = cantidad_votaciones_por_region(lineas, region)
        resultados_region[region] = votaciones_region

    region_mayor_participacion, votos_mayor_participacion = resultados_region.most_common(1)[0]

    porcentaje_mayor_participacion = (votos_mayor_participacion / len(lineas)) * 100

    return region_mayor_participacion, porcentaje_mayor_participacion

def verificar_segunda_vuelta_bogota(lineas, ciudad_bogota, candidatos):
    votos_candidatos_bogota = {candidato: 0 for candidato in candidatos}

    for linea in lineas:
        if ciudad_bogota in linea:
            datos = linea.strip().split(',')
            candidato = datos[0]
            votos_candidatos_bogota[candidato] += 1

    total_votos_bogota = sum(votos_candidatos_bogota.values())
    
    primer_candidato = max(votos_candidatos_bogota, key=votos_candidatos_bogota.get)
    segundo_candidato = sorted(votos_candidatos_bogota, key=votos_candidatos_bogota.get, reverse=True)[1]

    porcentaje_primero = (votos_candidatos_bogota[primer_candidato] / total_votos_bogota) * 100
    porcentaje_segundo = (votos_candidatos_bogota[segundo_candidato] / total_votos_bogota) * 100

    # Mostrar el porcentaje de cada candidato
    print(f"Porcentaje de votos para {primer_candidato}: {porcentaje_primero:.2f}%")
    print(f"Porcentaje de votos para {segundo_candidato}: {porcentaje_segundo:.2f}%")

    # Verificar condiciones para la primera vuelta
    if porcentaje_primero >= 40 and porcentaje_primero - porcentaje_segundo >= 10:
        return False, None, None
    else:
        return True, primer_candidato, segundo_candidato


def contar_genero_votantes(lineas):
    genero_votantes = Counter()

    for linea in lineas:
        datos = linea.strip().split(',')
        genero = datos[-1]
        genero_votantes[genero] += 1

    return genero_votantes


def main():
    
    ciudades=['Bogotá', 'Barranquilla', 'Cali', 'Medellín', 'Bucaramanga', 'Pasto', 'Cartagena']
    regiones=['Caribe', 'Centro', 'Sur']
    partidos=['Partido1', 'Partido2', 'Partido3']
    candidatos=['Candidato1', 'Candidato2', 'Candidato3', 'Candidato4']
    sitios=['Sitio1', 'Sitio2','Sitio3']
    mesas=['Mesa1', 'Mesa2', 'Mesa3', 'Mesa4']
    genero=['Hombre','Mujer']
    

     # Eliminar el archivo existente antes de escribir uno nuevo
    with open("votacion1.txt", 'w'):
        pass

#Candidato,partido,ciudad,sitio,mesa,genero
    
    archivo = open("votacion1.txt",'a')
    n=int(input("Digite la cantidad de votaciones: "))
    for cant in range(n):
        
        linea= random.choice(candidatos)+","+ random.choice(partidos)+ ","+ random.choice(ciudades)+ "," + random.choice(sitios) + "," + random.choice(mesas)  + "," + random.choice(genero) 
        print(linea)
        archivo.write(linea)
        archivo.write("\n")
    archivo.close()

    # Volver a abrir el archivo en modo de lectura
    with open("votacion1.txt", 'r') as archivo:
        # Leer las líneas del archivo
        lineas = archivo.readlines()

    # Ejemplo de cómo utilizar las funciones
    total_votaciones = cantidad_votaciones_pais(lineas)
    print(f"Total de votaciones en el país: {total_votaciones}")

    for ciudad in ciudades:
        votaciones_ciudad = cantidad_votaciones_por_ciudad(lineas, ciudad)
        print(f"Total de votaciones en {ciudad}: {votaciones_ciudad}")

        for candidato in candidatos:
            votos_candidato_ciudad = cantidad_votos_por_candidato_ciudad(lineas, candidato, ciudad)
            print(f"Votos para {candidato} en {ciudad}: {votos_candidato_ciudad}")
    
    for region in regiones:
        votaciones_region = cantidad_votaciones_por_region(lineas, region)
        print(f"Total de votaciones en la región {region}: {votaciones_region}")
    
    for ciudad in ciudades:
        ganador = ganador_por_ciudad(lineas, ciudad)
        print(f"Ganador en {ciudad}: {ganador}")
    
    for partido in partidos:
        votos_partido = votacion_por_partido(lineas, partido)
        print(f"Votación para el partido {partido}: {votos_partido}")
    
    resultados_por_partido_ciudad = votacion_por_partido_ciudad(lineas,ciudades)
    for ciudad, resultados_ciudad in resultados_por_partido_ciudad.items():
        print(f"Votación por partido en {ciudad}: {resultados_ciudad}")

    resultados_por_partido_region = votacion_por_partido_region(lineas,region)
    for region, resultados_region in resultados_por_partido_region.items():
        print(f"Votación por partido en la región {region}: {resultados_region}")

    resultados_sitio_ciudad = sitio_con_mayor_votacion_por_ciudad(lineas, ciudades)
    for ciudad, sitio in resultados_sitio_ciudad.items():
        print(f"Sitio con mayor votación en {ciudad}: {sitio}")
    
    ciudad_mayor_votacion, porcentaje_mayor_votacion = ciudad_con_mayor_votacion(lineas, ciudades)
    print(f"Ciudad con mayor votación: {ciudad_mayor_votacion}")
    print(f"Porcentaje de votación: {porcentaje_mayor_votacion:.2f}%")

    region_mayor_participacion, porcentaje_mayor_participacion = region_con_mayor_participacion(lineas, regiones)
    print(f"Región con mayor participación: {region_mayor_participacion}")
    print(f"Porcentaje de participación: {porcentaje_mayor_participacion:.2f}%")
    
    hay_segunda_vuelta, primer_candidato, segundo_candidato = verificar_segunda_vuelta_bogota(lineas, 'Bogotá', candidatos)

    if hay_segunda_vuelta:
        print("Habrá segunda vuelta en Bogotá.")
        print(f"Candidatos: {primer_candidato} y {segundo_candidato}")
    else:
        print("No habrá segunda vuelta en Bogotá.")
   

    # Obtener la cantidad de mujeres y hombres que votaron
    genero_votantes = contar_genero_votantes(lineas)
    
    # Mostrar la cantidad de mujeres y hombres
    print(f"Cantidad de mujeres que votaron: {genero_votantes['Mujer']}")
    print(f"Cantidad de hombres que votaron: {genero_votantes['Hombre']}")

main()   




