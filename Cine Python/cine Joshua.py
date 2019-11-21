def main():
    c1 = Cliente("Carlos","123-123456-1234A", 23)
    c2 = Cliente("Esteban","321-654321-4321B", 23)
    c3 = Cliente("Jose", "098-098765-0987C", 23)
    s = Sala(1, "Anaconda3", 20)
    s.mostrarInfoClientes()
    s.agregarCliente(c1)
    s.mostrarInfoClientes()
    s.agregarCliente(c2)
    s.agregarCliente(c3)
    s.mostrarInfoClientes()

class Cliente():
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

class Sala():
    def __init__(self, cantidadAsientos, nombrePelicula, precioEntrada):
        self.cantidadAsientos = cantidadAsientos
        self.nombrePelicula = nombrePelicula
        self.precioEntrada = precioEntrada
        self.Clientes = []

    def agregarCliente(self, Cliente):
        if len(self.Clientes) != self.cantidadAsientos:
            self.Clientes.append(Cliente)
            print("Se ha agregado un cliente a la sala!", end="\n\n")
        else:
            print("No se ha agregado el cliente! La sala se encuentra llena!", end="\n\n")

    def mostrarInfoClientes(self):
        if len(self.Clientes) == 0:
            print("La sala se encuentra vacia!", end="\n\n")
        else:
            for i in range(len(self.Clientes)):
                print("Información de cliente de la sala: ")
                print("Cliente " + str((i+1)) + ": " + self.Clientes[i].nombre + ", " + self.Clientes[i].cedula + ", " + str(self.Clientes[i].edad))
            print()

if __name__ == "__main__":
    main()