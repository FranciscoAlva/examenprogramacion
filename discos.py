import sqlite3
import sys 

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
        artista = input("Introduce el artista: ")
        anio = input("Introduce el año: ")
        titulo = input("Introduce el título: ")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "INSERT INTO discos VALUES (NULL,'"+artista+"',"+str(anio)+",'"+titulo+"')"
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
        print("Tu resgistro de guardo correctamente")
        
    elif opcion == "2":
        print("Mostramos los registros")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "SELECT * FROM discos"
        cursor.execute(peticion)
        while True:
            fila = cursor.fetchone()
            if fila is None:
                break
            print(fila)
        conexion.commit()
        conexion.close()
        
    elif opcion == "3":
        print("Modificamos los registros")
        Identificador = input("Introduce el Id: ")
        artista = input("Introduce el artista: ")
        anio = input("Introduce el año: ")
        titulo = input("Introduce el título: ")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "UPDATE discos SET artista = '"+artista+"',anio="+anio+",titulo='"+titulo+"' WHERE Identificador="+Identificador+""
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
        print("Tu resgistro se modifico correctamente")
        
        
    elif opcion == "4":
        print("Eliminamos los registros")
        Identificador = input("Introduce el Id del registro a eliminar: ")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "DELETE FROM discos WHERE Identificador = "+Identificador+""
        cursor.execute(peticion)
        conexion.commit()
        conexion.close()
        
    elif opcion == "5":
        print("Buscamos los registros")
        artista = input("Introduce el nombre del artista: ")
        conexion = sqlite3.connect("discos.db")
        cursor = conexion.cursor()
        peticion = "SELECT * FROM discos WHERE artista LIKE '%"+artista+"%'"
        cursor.execute(peticion)
        contador = 0
        while True:
            encontrado = True
            contador += 1
            fila = cursor.fetchone()
            if fila is None:
                break
            print(fila)
        if contador < 2:
            print("No se encontro ningun registro")
        conexion.commit()
        conexion.close()
        
    elif opcion == "6":
        print("Salimos del programa")
        sys.exit()
        
    #menurecursivo
    menu()
menu()
    
