"""Ejercicio 2"""


class Vuelo():
    def __init__(self, numero, horaSalida, horaLlegada):
        self.numero = numero
        self.horaSalida = horaSalida
        self.horaLlegada = horaLlegada
        
    def estado(self):
        print(str(self.numero), self.horaSalida, self.horaLlegada)
        
class VCarga(Vuelo):
    def __init__(self, numero, horaSalida, horaLlegada, pesoMax):
        super().__init__(numero, horaSalida, horaLlegada)
        self.pesoMax = pesoMax
        
    def imprimirPeso(self):
        print("El peso máximo del vuelo es: ",self.pesoMax)
 
        
class VComercial(Vuelo):
    def __init__(self, numero, horaSalida, horaLlegada):
        super().__init__(numero, horaSalida, horaLlegada)
        self.pasajeros = []
    
    def Agregarpasajero(self, Pasajero):
        self.pasajeros.append(Pasajero)
        print(pasajeros)
        
    def Quitarpasajeros(self, Pasajero):
        self.pasajero.remove(Pasajero)
        
class VLocal(VComercial):
    def __init__(self, numero, horaSalida, horaLlegada, minPasajeros):
        super().__init__(numero, horaSalida, horaLlegada)
        self.minPasajeros = minPasajeros
        
class VInternacional(VComercial):
    def __init__(self, numero, horaSalida, horaLlegada, paisDestino):
        super().__init__(numero, horaSalida, horaLlegada)
        self.paisDestino = paisDestino
      
class Pasajero(VComercial):
    def __init__(self, numero, horaSalida, horaLlegada, codigo, nombre, precio, impuesto, descuento):
        super().__init__(numero, horaSalida, horaLlegada)
        self.precio = precio
        self.impuesto = impuesto
        self.descuento = descuento
      
        
    def Totalpagar(self):
        Totalpagar =  self.precio + (self.precio * self.impuesto) 
        Totalpagar = Totalpagar - (Totalpagar * self.descuento)
        return(Totalpagar)
        
class PasajeroF(Pasajero):
    def __init__(self, numero, horaSalida, horaLlegada, codigo, nombre, precio, impuesto): 
        self.descuento = 0.20
        super().__init__(numero, horaSalida, horaLlegada, codigo, nombre, precio, impuesto, self.descuento)
        
            
class PasajeroNF(Pasajero):
    def __init__(self, numero, horaSalida, horaLlegada, codigo, nombre, precio, impuesto):
        self.descuento = 0.05
        super().__init__(numero, horaSalida, horaLlegada, codigo, nombre, precio, impuesto, self.descuento)
                 

      
            
            
pasa1= PasajeroF(45,"Entrada", "Salida",4, "Juan",45,5)
pasa1.estado()
print(pasa1.Totalpagar())

pasa2= PasajeroNF(45,"Entrada", "Salida",4, "Pedro",45,5)
pasa2.estado()
print(pasa2.Totalpagar())