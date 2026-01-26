# facturacion/repositorio_facturas.py
import os

class RepositorioFacturas:
    """
    Clase encargada de manejar el almacenamiento de facturas.
    El archivo facturas_emitidas.txt se crea en la carpeta raíz del proyecto.
    """

    def __init__(self, nombre_archivo: str = "facturas_emitidas.txt"):
        # CONSTRUCTOR
        # Se ejecuta al crear el objeto

        # Obtiene la ruta del archivo actual (facturacion/)
        ruta_actual = os.path.dirname(__file__)

        # Sube un nivel para llegar a la carpeta raíz del proyecto
        ruta_proyecto = os.path.abspath(os.path.join(ruta_actual, ".."))

        # Ruta final del archivo en el proyecto principal
        self.ruta_archivo = os.path.join(ruta_proyecto, nombre_archivo)

        # Abre el archivo (recurso externo)
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