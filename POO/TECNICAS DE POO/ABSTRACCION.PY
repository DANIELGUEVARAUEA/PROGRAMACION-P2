# ==============================
#   CLASE ABSTRACCIÓN
# ==============================

class Factura:           #clase factura
    def __init__(self, numero):
        self._numero = numero       # Encapsulamiento (protegido)
        self.__items = []           # Encapsulamiento (privado)

    def agregar_item(self, descripcion, precio, cantidad):
        self.__items.append({
            "descripcion": descripcion,
            "precio": precio,
            "cantidad": cantidad
        })

    def _subtotal(self):
        return sum(item["precio"] * item["cantidad"] for item in self.__items)

    def total(self):
        
        raise NotImplementedError("Debe implementarse en la subclase.")

    def mostrar(self):
        """Mostrar datos generales; es parte de la abstracción."""
        print(f"Factura Nº {self._numero}")
        print("Subtotal:", self._subtotal())


# ==============================
#   HERENCIA + POLIMORFISMO
# ==============================

class FacturaConIVA(Factura):
    def __init__(self, numero, iva=0.15):
        super().__init__(numero)
        self.iva = iva

    def total(self):
        """Polimorfismo: cálculo propio"""
        subtotal = self._subtotal()
        return subtotal + subtotal * self.iva


class FacturaExenta(Factura):
    def total(self):
        """Polimorfismo: no tiene IVA"""
        return self._subtotal()


# ==============================
#        USO DEL PROGRAMA
# ==============================

# Factura normal con IVA 15
f1 = FacturaConIVA("A-0000-100")
f1.agregar_item("Producto A", 100, 2)
f1.agregar_item("Producto B", 50, 1)

# Factura iva cero
f2 = FacturaExenta("B-0000-200")
f2.agregar_item("viveres", 80, 3)

# Mostramos ambas
f1.mostrar()
print("TotalIVA 15:", f1.total(), "\n")

f2.mostrar()
print("Total iva 0:", f2.total())
