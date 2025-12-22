# Importar las clases desde sus respectivos archivos
from cliente import Cliente
from habitacion import Habitacion
from reserva import Reserva

def main():
    print("=== SISTEMA DE RESERVAS DEL HOTEL ===\n")

    # Solicitar datos del cliente
    nombre = input("Ingrese el nombre del cliente: ")
    cedula = input("Ingrese la cédula del cliente: ")

    # Crear objeto Cliente
    cliente = Cliente(nombre, cedula)

    # Solicitar datos de la habitación
    numero = int(input("\nIngrese el número de la habitación: "))
    tipo = input("Ingrese el tipo de habitación (Simple / Doble / Suite): ")
    precio = float(input("Ingrese el precio por noche: "))

    # Crear objeto Habitacion
    habitacion = Habitacion(numero, tipo, precio)

    # Solicitar días de hospedaje
    dias = int(input("\nIngrese la cantidad de días de hospedaje: "))

    # Crear objeto Reserva
    reserva = Reserva(cliente, habitacion, dias)

    # Confirmar la reserva
    print("\n--- DETALLE DE LA RESERVA ---")
    print(reserva.confirmar_reserva())

# Punto de entrada del programa
if __name__ == "__main__":
    main()
