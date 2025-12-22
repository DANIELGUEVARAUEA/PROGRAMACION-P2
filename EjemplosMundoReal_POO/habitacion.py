class Habitacion:
    def __init__(self, numero, tipo, precio):
        # Atributos de la habitación
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # Estado inicial de la habitación

    def reservar(self):
        # Método que cambia el estado de disponibilidad
        self.disponible = False

    def liberar(self):
        # Método que vuelve a dejar la habitación disponible
        self.disponible = True
