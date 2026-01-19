# Clase principal base la Factura
# Ejemplo de una factura de un restaurante

class Factura:
    def __init__(self, cliente, subtotal):
                                       # Encapsulación: atributos protegidos
        self._cliente = cliente
        self._subtotal = subtotal

    def calcular_total(self):
        
        #Método que será sobrescrito por las clases hijas. Aplicando polimorfismo.
       
        raise NotImplementedError("Este método debe ser implementado por la clase hija")

    def mostrar_resumen(self):
        return f"Cliente: {self._cliente} | Subtotal: ${self._subtotal:.2f}"
