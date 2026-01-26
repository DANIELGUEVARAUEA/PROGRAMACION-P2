# main.py
import gc
from modelos.repositorio_facturas import RepositorioFacturas
from servicios.facturacion_service import FacturacionService

def main():
    print("=== Sistema de Facturación ===")

    # __init__: se crea el repositorio y se abre el archivo
    repositorio = RepositorioFacturas()
    servicio = FacturacionService(repositorio)

    while True:
        print("\n--- Menú ---")
        print("1. Emitir factura")
        print("2. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            # SOLO se pide el nombre del cliente
            cliente = input("Nombre del cliente: ").strip()

            if not cliente:
                print("El nombre no puede estar vacío.")
                continue

            # Total fijo para simplificar el ejemplo
            total = 100.00

            # Se crea una nueva factura (objeto inmutable)
            factura = servicio.emitir_factura(cliente, total)

            print("\n Factura emitida correctamente")
            print(factura)

        elif opcion == "2":
            print("\nSaliendo del sistema...")
            break

        else:
            print(" Opción no válida")

    # Cierre explícito del archivo 
    repositorio.cerrar()

    # Eliminamos el objeto para evidenciar el destructor
    del repositorio
    gc.collect()

    print("Programa finalizado.")

if __name__ == "__main__":
    main()