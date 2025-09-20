# Función en la cual se calcula el descuento
def procesa_descuento(monto_total, porcentaje_descuento =10):    #PARAMETROS
    descuento = monto_total * (porcentaje_descuento / 100)       #OPERACION PARA EL DESCUENTO
    return descuento                                             #DEVUELVE EL VALOR DEL DESCUENTO


# Programa

# Primer llamado con el valor por defecto (10%)
monto1 = float(input("Ingrese el total de la primera compra: "))   #INGRESO EL VALOR 1 A CALCULAR
descuento1 = procesa_descuento(monto1)                             #VALOR DE LOS ARGUMENTOS PRIMER LLAMADO
total1 = monto1 - descuento1                                        #RESTAMOS EL TOTAL1 MENOS DESCUENTO

# Segundo llamado se ingresa también el porcentaje
monto2 = float(input("Ingrese el total de la segunda compra: "))                        #INGRESA EL VALOR 2 A CALCULAR
porcentaje2 = int(input("Ingrese el porcentaje de descuento de su segunda compra: "))   #INGRESA EL PORCENTAJE DEL DESCUENTO

descuento2 = procesa_descuento(monto2,porcentaje2)                                      #VALOR DE LOS ARGUMENTOS SEGUNDO LLAMADO
total2 = monto2 - descuento2                                                            #RESTAMOS EL TOTAL2 MENOS DESCUENTO


#MUESTRA EN PANTALLA LOS DOS LLAMADOS

print("\nPrimera compra:")
print(f"Subtotal: ${monto1:.2f}")
print(f"Descuento aplicado (10%): ${descuento1:.2f}")
print(f"Total a pagar compra1: ${total1:.2f}")
print("************************")

print("\nSegunda compra:")
print(f"Monto total: ${monto2:.2f}")
print(f"Descuento aplicado ({porcentaje2}%): ${descuento2:.2f}")
print(f"Total a pagar compra2: ${total2:.2f}")