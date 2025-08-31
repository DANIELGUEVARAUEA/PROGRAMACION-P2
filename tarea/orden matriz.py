
# Matriz notas 3x3
matriz = [
    [8, 7, 9],  # Notas estudiante 1
    [10, 11, 12],  # Notas estudiante 2
    [15, 20, 18]  # Notas estudiante 3
]

# imprime la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Función para ordenar la matriz usando Bubble Sort
    def bubble_sort(matriz):
        for fila in matriz:
            for i in range(len(fila)):
                for j in range(len(fila) - i - 1):
                    if fila[j] > fila[j + 1]:
                        fila[j], fila[j + 1] = fila[j + 1], fila[j]

# llamamos la funcion para Ordenar toda la matriz
bubble_sort(matriz)

# Mostrar la matriz con las filas ordenadas
print("\nMatriz ordenada:")
for fila in matriz:
    print(fila)