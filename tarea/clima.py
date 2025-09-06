# días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# ingresamos las temperaturas diarias para cada ciudad durante 4 semanas
# Cada ciudad tiene 7 temperaturas  durante 4 semanas
temperaturas = [
    [  # Datos Quito
        [20, 19, 18, 19, 20, 21, 22],  # Semana 1
        [19, 18, 17, 18, 19, 20, 21],  # Semana 2
        [20, 20, 19, 18, 19, 20, 21],  # Semana 3
        [21, 20, 19, 20, 21, 22, 23],  # Semana 4
    ],
    [  # Datos Guayaquil
        [31, 32, 33, 32, 31, 30, 29],  # Semana 1
        [32, 33, 34, 33, 32, 31, 30],  # Semana 2
        [33, 34, 35, 34, 33, 32, 31],  # Semana 3
        [32, 33, 34, 33, 32, 31, 30],  # Semana 4
    ],
    [  # Datos Cuenca
        [18, 19, 20, 19, 18, 17, 16],  # Semana 1
        [19, 20, 21, 20, 19, 18, 17],  # Semana 2
        [20, 21, 22, 21, 20, 19, 18],  # Semana 3
        [21, 22, 23, 22, 21, 20, 19],  # Semana 4
    ]
]

# Función para calcular el promedio de temperaturas en una semana
def calcular_prom(temp_semanales):
    return sum(temp_semanales) / len(temp_semanales) #realizamos la operacion suma y con len contamos los dias en este caso 7

# Mostrar las temperaturas diarias y los promedios
for i, ciudad in enumerate(["Quito", "Guayaquil", "Cuenca"]):     #se obtiene los indices
    print(f"\nTemperaturas diarias para {ciudad}:")
    for semana in range(4):                    #recorre 0,1,2,3
        print(f"\nSemana {semana + 1}:")
        for dia, temp in zip(dias, temperaturas[i][semana]): # se combina dias con la temperatura
            print(f"{dia}: {temp}Grados Centigrados")
        promedio = calcular_prom(temperaturas[i][semana])
        print(f"Promedio de la semana {semana + 1}: {promedio:.2f}  Grados Centigrados")
    print("\n")
