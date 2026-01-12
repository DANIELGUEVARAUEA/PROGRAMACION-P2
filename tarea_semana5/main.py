""
#llamamos a nuestra clase 
from convertidor import ConvertidorTemperatura

def main():
    # Entrada de datos
    temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

    # Crear objeto de la clase
    convertidor = ConvertidorTemperatura(temperatura_celsius)

    # Procesos
    temperatura_fahrenheit = convertidor.convertir_a_fahrenheit()
    clima_calido = convertidor.es_clima_calido()

    # Mensajes  tipo string
    mensaje = "El clima es cálido, Autor: Daniel Guevara." if clima_calido else "El clima es frio, Autor: Daniel Guevara"

    # Salida de resultados
    print("\nResultados:")
    print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit}")
    print(mensaje)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
