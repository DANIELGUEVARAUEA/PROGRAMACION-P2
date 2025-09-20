# Función en la cual se calcula el descuento
def procesa_descuento(monto_total, porcentaje_descuento =10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa

# Primer llamado con el valor por defecto (10%)
monto1 = float(input("Ingrese el total de la primera compra: "))
descuento1 = procesa_descuento(monto1)
total1 = monto1 - descuento1

# Segundo caso: el usuario ingresa también el porcentaje
monto2 = float(input("Ingrese el total de la segunda compra: "))
porcentaje2 = float(input("Ingrese el porcentaje de descuento de su segunda compra: "))

descuento2 = procesa_descuento(monto2, porcentaje2)
total2 = monto2 - descuento2


#impreme los 2 casos

print("\nPrimera compra:")
print(f"Subtotal: ${monto1:.2f}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Total a pagar compra1: ${total1:.2f}")
print("************************")

print("\nSegunda compra:")
print(f"Monto total: ${monto2:.2f}")
print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
print(f"Total a pagar compra2: ${total2:.2f}")