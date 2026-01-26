# facturacion/repositorio_facturas.py
import os

class RepositorioFacturas:
    """
    Clase encargada de manejar el almacenamiento de facturas.
    Demuestra el uso de __init__ y __del__ con un recurso real (archivo).
    """

    def __init__(self, ruta_archivo: str = "facturacion/facturas_emitidas.txt"):
        # CONSTRUCTOR
        # Se ejecuta al crear el objeto y abre el archivo
        self.ruta_archivo = ruta_archivo

        # Crea la carpeta 'facturacion' si no existe
        os.makedirs(os.path.dirname(self.ruta_archivo), exist_ok=True)

        # Abre el archivo dentro de la carpeta facturacion
        self._archivo = open(self.ruta_archivo, "a", encoding="utf-8")
        self._abierto = True

        self._archivo.write("[INIT] Repositorio de facturas iniciado.\n")
        self._archivo.flush()

    def guardar(self, factura) -> None:
        # Guarda una factura en el archivo
        if not self._abierto:
            raise RuntimeError("El archivo está cerrado.")

        linea = f"{factura.numero} | {factura.fecha} | {factura.cliente} | ${factura.total:.2f}\n"
        self._archivo.write(linea)
        self._archivo.flush()

    def cerrar(self) -> None:
        # Cierre explícito del archivo (buena práctica)
        if self._abierto:
            self._archivo.write("[CLOSE] Archivo cerrado manualmente.\n")
            self._archivo.close()
            self._abierto = False

    def __del__(self):
        # DESTRUCTOR
        # Se ejecuta cuando el objeto es destruido o al finalizar el programa
        try:
            if hasattr(self, "_abierto") and self._abierto:
                self._archivo.write("[DEL] Destructor ejecutado. Cerrando archivo.\n")
                self._archivo.close()
                self._abierto = False
        except Exception:
            pass