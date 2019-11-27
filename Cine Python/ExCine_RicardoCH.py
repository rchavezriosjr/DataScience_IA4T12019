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
        
    def addCliente(self, Cliente):
        if len(self.Clientes) != self.cantidadAsientos:
            self.Clientes.append(Cliente)
            print("Agregado", end="\n\n")
        else:
            print("Error: Sala llena.", end="\n\n")
            
    def infoClientes(self):
        if len(self.Clientes) == 0:
            print("Sala vacia", end="\n\n")
        else:
            print("Clientes en sala:")
            for i in range(len(self.Clientes)):
                print("Cliente " + str((i+1)) + ": "+ self.Clientes[i].nombre + ", "+ self.Clientes[i].cedula + ", " + str(self.Clientes[i].edad))
            print()

def main():
    c1 = Cliente("Ricardo","401-020599-1000K",20)
    c2 = Cliente("Harold","001-123456-4000K",24)
    c3 = Cliente("Bismark","001-123456-4000K", 20)
    s = Sala(2,"Sala 3D", 50)
    s.infoClientes()
    s.addCliente(c1)
    s.infoClientes()
    s.addCliente(c2)
    s.infoClientes()
    s.addCliente(c3)
    s.infoClientes()

if __name__ == "__main__":
    main()