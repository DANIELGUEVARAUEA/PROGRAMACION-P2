# modelos/factura.py
from dataclasses import dataclass
from datetime import datetime

# @dataclass genera automáticamente el __init__, __repr__, __eq__, etc.
# frozen=True hace que la factura sea INMUTABLE (no se puede modificar luego)
@dataclass(frozen=True)
class Factura:
    # Atributos de la factura
    numero: int        # Número único de factura
    cliente: str       # Nombre del cliente
    total: float       # Monto total
    fecha: str         # Fecha de emisión

    @staticmethod
    def crear(numero: int, cliente: str, total: float) -> "Factura":
        # Método de fábrica:
        # Se usa para centralizar la creación de facturas
        # Genera la fecha automáticamente
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return Factura(numero, cliente, total, fecha)