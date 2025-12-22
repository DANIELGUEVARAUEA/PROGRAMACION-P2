class Reserva:
    def __init__(self, cliente, habitacion, dias):
        # Atributos de la reserva
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias

    def confirmar_reserva(self):
        # Verifica si la habitación está disponible
        if self.habitacion.disponible:                          #Condicion para disponibilidad
            self.habitacion.reservar()
            total = self.habitacion.precio * self.dias
            return (
                f"Reserva confirmada\n"
                f"{self.cliente.mostrar_info()}\n"
                f"Habitación: {self.habitacion.numero} ({self.habitacion.tipo})\n"
                f"Días: {self.dias}\n"
                f"Total a pagar: ${total}"
            )
        else:
            return "La habitación no está disponible"
