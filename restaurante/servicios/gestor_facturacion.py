# Clase que gestiona las facturas del restaurante

class GestorFacturacion:
    def __init__(self):
        self.facturas = []

    def agregar_factura(self, factura):
        # Polimorfismo: acepta cualquier objeto que herede de Factura
        self.facturas.append(factura)

    def mostrar_facturas(self):
        for factura in self.facturas:
            print(factura.mostrar_resumen())
            print(f"Total a pagar: ${factura.calcular_total():.2f}")
            print("-" * 15)
