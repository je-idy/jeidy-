# Definir la matriz 3D de temperaturas: [ciudad][día de la semana][semana]
# Suponiendo 2 ciudades, 7 días de la semana, y 2 semanas
temperaturas = [
    # Quito
    [
        [20, 21, 19, 22, 20, 21, 23],  # Semana 1
        [22, 23, 21, 20, 24, 25, 26]   # Semana 2
    ],
    # Guayaquil
    [
        [18, 19, 17, 21, 20, 18, 22],  # Semana 1
        [20, 22, 19, 23, 21, 22, 24]   # Semana 2
    ]
]

# Calcular y mostrar el promedio de temperaturas para cada ciudad por semana
ciudades = ['Quito', 'Guayaquil']
semanas = ['Semana 1', 'Semana 2']

for i in range(len(temperaturas)):
    print(f"\nPromedios de {ciudades[i]}:")
    for j in range(len(temperaturas[i])):
        suma_temperaturas = sum(temperaturas[i][j])
        promedio = suma_temperaturas / len(temperaturas[i][j])
        print(f"{semanas[j]}: {promedio:.2f} °C")