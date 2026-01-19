from modelos.factura import Factura

# Clase derivada que representa una factura de consumo en restaurante
class FacturaConsumo(Factura):
    def __init__(self, cliente, subtotal):
        # Llamada al constructor de la clase base
        super().__init__(cliente, subtotal)

    # Polimorfismo: implementación específica del cálculo
    def calcular_total(self):
        iva = self._subtotal * 0.15
        servicio = self._subtotal * 0.10
        total = self._subtotal + iva + servicio
        return total

    def mostrar_resumen(self):
        return f"{super().mostrar_resumen()} | Tipo: Consumo"
