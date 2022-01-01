import sys
#ten cuidado no pongas ";" pon ":"
def menu():
    phone_book = {}
    while True:
        print('''
        1. Mostrar lista de contactos.
        2. Añadir contacto (nombre y teléfono).
        3. Borrar contacto (nombre).
        4. Salir.
        ''')

        menu = input("¿Que acción que desea realizar?: ")
# opcion del menú 1
        if menu == '1':
            show_contacts(phone_book)

# opcion del menu 2
        elif menu == '2':
            name = input("Nombre del contacto: ")
            if name not in phone_book:
                phone = input("Número de teléfono (movil o fijo): ")
                add_contact(phone_book, name, phone)
            else:
                print("Ya esta registrado :3. ")
# opcion 3 del menu

        elif menu == '3':
            name = input("Nombre del contacto que desea eliminar: ")
            if name in phone_book:
                remove_contact(phone_book, name)
            else:
                print("El contacto que desea eliminar no se encuentra en su lista de contactos. ")
# mi loco para fuera
        elif menu == '4':
            break
#En caso de que la gente no sepa leer que escoja 1, 2, 3 o 4.
        elif menu > '4':
            print("No entiendo que quiere hacer :C :")

def show_contacts(phone_book):
    if phone_book == {}:
        print("La agenda está vacía. Por favor, agregue contactos para poder usar las funciones del menú.")
    else:
        for name, phone in phone_book.items():
            print(name, ":", phone)
#sentencia para añadir contactos
def add_contact(phone_book, name, phone):
    phone_book[name] = phone
# sentencia para borrar (ya funciona ^^)
def remove_contact(phone_book, name):
    del(phone_book[name])

if __name__ == '__main__':
    menu()