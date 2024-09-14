def calcular_temperatura_promedio(ciudades_temperaturas):
    """
    Calcula la temperatura promedio de múltiples ciudades durante varias semanas.

    Parámetros:
    ciudades_temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades (str)
                                  y los valores son listas de temperaturas semanales (list of list of float).

    Retorna:
    dict: Un diccionario con las ciudades como claves y sus temperaturas promedio como valores.
    """

    # Diccionario para almacenar las temperaturas promedio de cada ciudad
    promedios = {}

    # Iterar sobre cada ciudad en el diccionario
    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Inicializar la suma total de temperaturas y el conteo de semanas
        suma_total = 0
        semanas = len(temperaturas)

        # Iterar sobre cada semana de temperaturas
        for semana in temperaturas:
            # Sumar las temperaturas de cada semana
            suma_total += sum(semana)

        # Calcular el número total de mediciones de temperatura
        total_mediciones = semanas * len(temperaturas[0])  # Número de semanas * mediciones por semana

        # Calcular la temperatura promedio de la ciudad
        promedio = suma_total / total_mediciones

        # Guardar el promedio en el diccionario
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso con las ciudades Quito, Guayaquil y Cuenca
datos_temperaturas = {
    'Quito': [
        [18.0, 17.5, 18.2, 17.8],  # Semana 1
        [17.9, 18.1, 18.3, 17.6],  # Semana 2
        [18.4, 17.8, 18.1, 18.0],  # Semana 3
        [17.7, 18.2, 18.3, 17.9],  # Semana 4
    ],
    'Guayaquil': [
        [29.0, 30.2, 29.5, 30.0],  # Semana 1
        [30.1, 29.9, 30.3, 29.8],  # Semana 2
        [30.5, 30.0, 29.7, 30.2],  # Semana 3
        [29.8, 30.4, 30.1, 29.9],  # Semana 4
    ],
    'Cuenca': [
        [15.0, 14.8, 15.2, 14.9],  # Semana 1
        [15.3, 15.0, 14.7, 15.1],  # Semana 2
        [14.9, 15.2, 14.8, 15.0],  # Semana 3
        [15.1, 15.4, 14.9, 15.2],  # Semana 4
    ],
}

# Llamar a la función y mostrar los resultados
promedios = calcular_temperatura_promedio(datos_temperaturas)
for ciudad, promedio in promedios.items():
    print(f"Temperatura promedio de {ciudad}: {promedio:.2f}°C")

