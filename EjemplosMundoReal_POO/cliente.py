class Cliente:
    def __init__(self, nombre, cedula):
        # Atributos del cliente
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_info(self):
        # Método que muestra la información del cliente
        return f"Cliente: {self.nombre}, Cédula: {self.cedula}"
