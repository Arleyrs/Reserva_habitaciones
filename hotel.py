class Habitacion:
    def __init__(self, numero, capacidad, precio):
        self.numero = numero
        self.capacidad = capacidad
        self.precio = precio
        self.reservada = False

    def __str__(self):
        return f"Habitación {self.numero} - Capacidad: {self.capacidad} - Precio: ${self.precio}"

    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

    def liberar(self):
        if self.reservada:
            self.reservada = False
            print(f"Habitación {self.numero} liberada.")
        else:
            print(f"Habitación {self.numero} no está reservada.")

    def calcular_costo(self, num_noches):
        return self.precio * num_noches

class HabitacionIndividual(Habitacion):
    def __init__(self, numero, precio):
        super().__init__(numero, 1, precio)

class HabitacionDoble(Habitacion):
    def __init__(self, numero, precio):
        super().__init__(numero, 2, precio)

# Crear habitaciones de ejemplo
habitacion1 = HabitacionIndividual(101, 100)
habitacion2 = HabitacionDoble(201, 150)
habitacion3 = HabitacionIndividual(102, 120)
habitacion4 = HabitacionDoble(202, 180)

habitaciones_disponibles = [habitacion1, habitacion2, habitacion3, habitacion4]

# Mostrar habitaciones disponibles
print("Habitaciones disponibles:")
for habitacion in habitaciones_disponibles:
    print(habitacion)

# Solicitar al usuario seleccionar una habitación
num_habitacion = int(input("Ingrese el número de la habitación que desea reservar: "))

habitacion_seleccionada = None
for habitacion in habitaciones_disponibles:
    if habitacion.numero == num_habitacion:
        habitacion_seleccionada = habitacion
        break

if habitacion_seleccionada:
    habitacion_seleccionada.reservar()
else:
    print("La habitación seleccionada no está disponible.")
