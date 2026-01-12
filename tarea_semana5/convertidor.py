#clase convertidor de temperatura

class ConvertidorTemperatura:
    def __init__(self, temperatura_celsius):
        # Atributo tipo float
        self.temperatura_celsius = temperatura_celsius

    def convertir_a_fahrenheit(self):
        """
        Convierte la temperatura de Celsius a Fahrenheit.
        Retorna un valor float.
        """
        return (self.temperatura_celsius * 9 / 5) + 32

    def es_clima_calido(self):
        """
        Determina si la temperatura en Fahrenheit corresponde a un clima cálido.
        Retorna un valor boolean.
        """
        temperatura_fahrenheit = self.convertir_a_fahrenheit()
        umbral_calido = 77  # tipo integer
        return temperatura_fahrenheit >= umbral_calido