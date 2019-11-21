#Sistema de ejemplo de para un Cine
#Con salas y clientes
#Elaborado por Jeffrey Josué Somarriba Molina
def main():
    c1 = Cliente(Moises,001-123456-1234A,20)
    c2 = Cliente(Joshua,001-654321-4321A,20)
    c3 = Cliente(Jeffrey, 001-191298-1025T, 20)
    s = Sala(2, El moisés, 50)
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
        print(Se ha agregado un cliente a la sala!, end=nn)
    else:
        print(No se ha agregado el cliente! La sala se encuentra llena!, end=nn)
        
def mostrarInfoClientes(self):
    if len(self.Clientes) == 0:
        print(La sala se encuentra vacia!, end=nn)
    else:
        for i in range(len(self.Clientes)):
            print(Mostrando información de clientes de la sala:)
            print(Cliente  + str((i+1)) + :  + self.Clientes[i].nombre + ,  + self.Clientes[i].cedula + ,  + str(self.Clientes[i].edad))
         print()

if __name__ == __main__:
    main()