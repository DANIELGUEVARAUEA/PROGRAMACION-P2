
# Aqui Abre el archivo en modo de lectura
with open('my_notes.txt', 'r') as file:
    # Lee cada línea del archivo y la muestra
    for line in file:
        print(line.strip())  # strip() elimina cualquier salto de línea extra

# El archivo se cierra automáticamente después de salir del bloque 'with'
# abre el documento en modo escritura
with open('my_notes.txt', 'a') as file:
    # Solicita al usuario que ingrese datos
    new_data = input("Escribe para agregar al archivo: ")
    # Escribe en el archivo
    file.write(new_data + '\n')  # Añade una nueva línea al final del archivo

print("Datos agregados correctamente.")

with open('my_notes.txt', 'r') as file:
    # Lee cada línea del archivo y la muestra
    for line in file:
        print(line.strip())  # strip() elimina cualquier salto de línea extra