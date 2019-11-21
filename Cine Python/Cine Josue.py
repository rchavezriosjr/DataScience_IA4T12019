class Customer:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"[{self.id:16} - {self.name:10} - {self.age:3}]"


class Room:
    def __init__(self, seating, movie, price):
        if seating % 2 == 0:
            self.seating = seating
            self.movie = movie
            self.price = price
            self.customers = list()
        else:
            print('La cantidad de asientos siempre debe se un numero par para este cine')

    def add(self, customer):
        if len(self.customers) < self.seating:
            self.customers.append(customer)
            print('\n\tMsg/> Cliente agregado!')
        else:
            print('\n\tErr/> La sala esta llena.')

    def show_everybody(self):
        value = '\t\t** Clientes **'
        for customer in self.customers:
            value = value + '\n' + customer.__str__()

        return value

    def takings(self):
        return self.price * len(self.customers)

    def free_seats(self):
        return self.seating - len(self.customers)

    def __str__(self):
        value = '\n=====================================' \
                f'\nPelicula {self.movie}' \
                f'\nPrecio {self.price}' \
                f'\nPlazas {self.seating}' \
                f'\nDisponible {self.free_seats()}' \
                f'\nTaquilla {self.takings()}' \
                '\n\n' + self.show_everybody() + '' \
                '\n=====================================\n'
        return value


print("*-*-*-*-*-*-*- Bienvenido al Cine por consola *-*-*-*-*-*-*-\n")
def menu():
    print('\n')
    print('1.- Crear una sala')
    print('2.- Comprar voleto')
    print('3.- Visualizar a los clientes')
    print('4.- Informacion de las salas')
    print('5.- Salir')

rooms = list()

def show_movies():
    value = '\n******** Salas ********\n'
    for i in range(len(rooms)):
        value += f'[{i+1}] ' + rooms[i].movie + '\n'
    print(value)

while True:
    menu()
    opc1 = int(input('>> '))

    if 0 < opc1 <= 5:
        if opc1 == 1:
            movie = input('Nombre de la Pelicula: ')
            seating = int(input('Plazas: '))
            price = float(input('Precio: '))
            room = Room(seating,movie,price)
            rooms.append(room)
            print('\n\tMsg/> Sala agregada')

        elif opc1 == 2:
            if len(rooms) > 0:

                if len(rooms) == 1:
                    print('Pelicula {}'.format(rooms[0].movie))
                    name = input('Nombre del cliente: ')
                    id = input('Id del Cliente: ')
                    age = int(input('Edad del Cliente: '))
                    customer = Customer(id, name, age)
                    rooms[0].add(customer)
                else:
                    show_movies()
                    opc2 = int(input('Que pelicula? #'))

                    if 0 < opc2 <= len(rooms):
                        opc2 = opc2 -1
                        name = input('Nombre del cliente: ')
                        id = input('Id del Cliente: ')
                        age = int(input('Edad del Cliente: '))
                        customer = Customer(id, name, age)
                        rooms[opc2].add(customer)
                    else:
                        print('\n\tErr/> Opcion Invalida')
            else:
                print('\n\tErr/> Aun no hay salas habilidatas')

        elif opc1 == 3:
            if len(rooms) > 0:

                if len(rooms) == 1:
                    print(rooms[0])
                else:
                    show_movies()
                    opc2 = int(input('Que pelicula? #'))

                    if 0 < opc2 <= len(rooms):
                        opc2 = opc2 - 1
                        rooms[opc2].show_everybody()
                    else:
                        print('\n\tErr/> Opcion Invalida')
            else:
                print('\n\tErr/> Aun no hay salas habilidatas')

        elif opc1 == 4:
            if len(rooms) > 0:
                print('\n\t********** Salas ************\n')
                for room in rooms:
                    print(room)
            else:
                print('\n\tErr/> Aun no hay salas habilidatas')
        else:
            break

# cus1 = Customer('001-171098-1039R', 'Josue', 21)
# cus2 = Customer('001-171098-1039R', 'David', 21)
# cus3 = Customer('001-171098-1039R', 'Reyes', 21)
# cus4 = Customer('001-171098-1039R', 'Molina', 21)
#
# room = Room(10, 'Zombies', 100.02)
# room.add(cus1)
# room.add(cus2)
# room.add(cus3)
# room.add(cus4)
#
# print(room)
