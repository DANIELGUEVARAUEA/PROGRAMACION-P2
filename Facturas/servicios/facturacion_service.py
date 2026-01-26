# facturacion/facturacion_service.py
from modelos.factura import Factura

class FacturacionService:
    """
    Servicio que contiene la lógica de negocio del sistema de facturación.
    """

    def __init__(self, repositorio):
        self.repositorio = repositorio
        self._contador = 1  # Numeración de facturas

    def emitir_factura(self, cliente: str, total: float) -> Factura:
        if not cliente.strip():
            raise ValueError("El cliente no puede estar vacío.")
        if total <= 0:
            raise ValueError("El total debe ser mayor a cero.")

        factura = Factura.crear(self._contador, cliente, total)
        self.repositorio.guardar(factura)
        self._contador += 1

        return factura