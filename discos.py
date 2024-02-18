#menu
def menu():
    print("Escoge una opcion: ")
    print("1.-Insertar un registro")
    print("2.-Mostrar registros")
    print("3.-Modificar un registro")
    print("4.-Eliminar un registro")
    print("5.-Buscar un registro")
    print("6.-Salir")
    opcion = input("Escoge una opcion: ")
    #if elif
    if opcion == "1":
        print("Insertamos un registro")
    elif opcion == "2":
        print("Mostramos los registros")
    elif opcion == "3":
        print("Modificamos los registros")
    elif opcion == "4":
        print("Eliminamos los registros")
    elif opcion == "5":
        print("Buscamos los registros")
    elif opcion == "6":
        print("Salimos del programa")
    menu()
menu()
    
