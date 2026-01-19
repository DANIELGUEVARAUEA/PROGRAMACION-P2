from modelos.factura_consumo import FacturaConsumo
from servicios.gestor_facturacion import GestorFacturacion

# Crear instancias de facturas
factura1 = FacturaConsumo("Daniel Guevara", 25.00)
factura2 = FacturaConsumo("Dayanna Porras", 68.76)

# Crear gestor de facturación
gestor = GestorFacturacion()

# Agregar facturas al gestor
gestor.agregar_factura(factura1)
gestor.agregar_factura(factura2)

# Mostrar resultados
gestor.mostrar_facturas()
