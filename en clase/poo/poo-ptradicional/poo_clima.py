class Clima:
    def __init__(self):
        self._temperaturas = []

    def ingresar_temperaturas(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves",
                "Viernes", "Sábado", "Domingo"]

        for dia in dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self._temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self._temperaturas) / len(self._temperaturas)


class ClimaSemanal(Clima):
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")
