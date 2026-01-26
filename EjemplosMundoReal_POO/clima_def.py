# Lista de días
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# matrices de temperaturas: Quito, Guayaquil, Cuenca (matriz de 4 semanas cada una)
temperaturas = [
    [  # Quito
        [20, 19, 18, 19, 20, 21, 22],
        [19, 18, 17, 18, 19, 20, 21],
        [20, 20, 19, 18, 19, 20, 21],
        [21, 20, 19, 20, 21, 22, 23],
    ],
    [  # Guayaquil
        [31, 32, 33, 32, 31, 30, 29],
        [32, 33, 34, 33, 32, 31, 30],
        [33, 34, 35, 34, 33, 32, 31],
        [32, 33, 34, 33, 32, 31, 30],
    ],
    [  # Cuenca
        [18, 19, 20, 19, 18, 17, 16],
        [19, 20, 21, 20, 19, 18, 17],
        [20, 21, 22, 21, 20, 19, 18],
        [21, 22, 23, 22, 21, 20, 19],
    ]
]

# Función 1 para calcular promedio de una semana
def calcular_prom(temp_semanales):
    return sum(temp_semanales) / len(temp_semanales) # retorna la suma y divide,por el numero de datos para el promedio, len cuenta los datos

# función 2 para mostrar temperaturas y promedios por ciudad
def mostrar_temperaturas(ciudades, temperaturas, dias): #definimos la funcion
    for i, ciudad in enumerate(ciudades): #for que recorra
        print(f"\n Temperaturas diarias para {ciudad}:")
        for semana in range(len(temperaturas[i])):
            print(f"\nSemana {semana + 1}:")
            for dia, temp in zip(dias, temperaturas[i][semana]): #es para conbinar los dias y la temperatura
                print(f"{dia}: {temp}°C")
            promedio = calcular_prom(temperaturas[i][semana])
            print(f" Promedio de la semana {semana + 1}: {promedio:.2f} °C") #muestra el resultado con 2 decimales


# Llamamos a la función y mostrar el resultado (sin este llamado no funciona)
ciudades = ["Quito", "Guayaquil", "Cuenca"]
mostrar_temperaturas(ciudades, temperaturas, dias)
