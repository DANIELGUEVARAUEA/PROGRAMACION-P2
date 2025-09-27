# Diccionario con información personal
informacion_personal = {"nombre": "Daniel Guevara","edad": 38,"ciudad": "Puyo",}

#mostramos en pantalla todos los datos en columna
print("Diccionario inicial")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# pedido para cambiar la ciudad
nueva_ciudad = input("Ingrese una nueva ciudad: ")
informacion_personal["ciudad"] = nueva_ciudad

# Ingresar una nueva clave y valor
nueva_clave = input("\nIngrese una nueva clave para el diccionario: ")
nuevo_valor = input(f"Ingrese el valor para '{nueva_clave}': ")
informacion_personal[nueva_clave] = nuevo_valor


# Verificacion si "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:                   #se realiza un if para cambiar el numero
    respuesta = input("La clave 'telefono' no existe. ¿Desea ingresarlo? (s/n): ").lower()
    if respuesta == "s":
        numero = input("Ingrese el número de teléfono: ")
        informacion_personal["telefono"] = numero

# Elimina la "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Muestra en pantalla el diccionario actualizado
print("\nDiccionario modificado:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")
