Lc = []
Lco = []
Li = []

def L_sector(p):
    if p[2] == "centro":
        Lc.append(p)
    elif p[2] == "colina":
        Lco.append(p)
    else:
        Li.append(p)

def Orden():
    cont_5k = 0
    cont_15k = 0
    cont_45k = 0

    Nombre_y_apellido = input("Ingrese su nombre y su apellido: ")
    Direccion = input("Ingrese su direccion: ")
    Comuna = input("Ingrese su sector (Centro, Colina o Industrias): ")
        
    while True:
        print("\n*** Tipos de Cilindros a elegir ***")
        print("1. Cilindros de 5kg")
        print("2. Cilindros de 15kg")
        print("3. Cilindros de 45kg")
        print("4. Volver atras.")

        eleccion = input("Que clase de cilindro(s) querra? \n: ")

        if eleccion == "1":
            cant_5kg = int(input("Ingrese cantidad de cilindros de 5kg\n: "))
            cont_5k += cant_5kg

        elif eleccion == "2":
            cant_15kg = int(input("Ingrese cantidad de cilindros de 15kg\n: "))
            cont_15k += cant_15kg

        elif eleccion == "3":
            cant_45kg = int(input("Ingrese cantidad de cilindros de 15kg\n: "))
            cont_45k += cant_45kg

        elif eleccion == "4":
            print("Regresando al menu principal\n")
            break
        else:
            print("Ingrese una opcion valida.")

        pedido = [Nombre_y_apellido,Direccion,Comuna.lower(),cont_5k,cont_15k,cont_45k]
        L_sector(pedido)

def texto(hoja):
    if hoja.lower() == "centro":
        if Lc == []:
            print("No hay entregas a realizar en el sector 'Centro'.")
        else:
            arch = open("Entregas sector Centro.txt", "w")
            for pe in Lc:
                arch.write(str(pe)+"\n")
            arch.close()
            print("Se ha creado el archivo con los datos de entrega. \n")

    elif hoja.lower() == "colina":
        if Lco == []:
            print("No hay entregas a realizar en el sector 'Colina'.")
        else:
            arch = open("Entregas sector Colina.txt", "w")
            for pe in Lco:
                arch.write(str(pe)+"\n")
            arch.close()
            print("Se ha creado el archivo con los datos de entrega. \n")

    elif hoja.lower() == "industria":
        if Li == []:
            print("No hay entregas a realizar en el sector 'Industrias'.")
        else:
            arch = open("Entregas sector Industrias.txt", "w")
            for pe in Li:
                arch.write(str(pe)+"\n")
            arch.close()
            print("Se ha creado el archivo con los datos de entrega. \n")



# *** MAIN ***

while True:
    print("Menu")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa\n")

    op = input("Ingrese opcion: ")

    if op == "1":
        Orden()

    elif op == "2":
        if Lc == [] and Lco == [] and Li == []:
            print("En este momento no se ha realizado ningun pedido a ningun sector.")
        else:
            print(Lc)
            print(Lco)
            print(Li)

    elif op == "3":
        Pedir_hoja = input("Que hoja de ruta desea convertir a archivo? (Centro, Colina o Industria) \n: ")
        texto(Pedir_hoja)

    elif op == "4":
        print("Saliendo del menu...\nBai")
        break

    else:
        print("Ingrese una opcion valida.")