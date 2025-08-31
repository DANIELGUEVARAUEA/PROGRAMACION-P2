# Definimos la matriz con las notas de 3 estudiantes de 3 materias
notas = [
    [8, 7, 9],  # Notas estudiante 1
    [10, 11, 12],  # Notas estudiante 2
    [15, 20, 18]  # Notas estudiante 3
]

# Función para buscar un valor en la matriz
def buscar(matriz, valor):
    for i in range(len(matriz)):  # Aqui recorre las filas
        for j in range(len(matriz[i])):  # Aqui recorre las columnas
            if matriz[i][j] == valor:  # La condicion Si encuentra el valor
                return (i, j)  # retorna la posición (fila, columna)
    return None  # Si no encuentra el numero

# primero imprimo los valores de la matriz para escoger

for fila in notas:
    print(fila)

# creamos una entrada para colocar el numero a consultar
valor_buscar = float(input("Ingrese el numero que desea buscar en la matriz: "))

# llamamos la funcion Buscar el valor en la matriz
resultado = buscar(notas, valor_buscar)

# Mostrar el resultado
if resultado:
    print(f"El valor {valor_buscar} Valor encontrado esta en la posición {resultado} (Fila {resultado[0] + 1}, Columna {resultado[1] + 1})")
else:
    print(f"El valor {valor_buscar} Valor no encontrado en la matriz.")