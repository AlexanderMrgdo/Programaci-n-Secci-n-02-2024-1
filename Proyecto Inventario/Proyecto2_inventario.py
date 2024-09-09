import json
data_inventario=[]
base_datos={}

#Funcion para asignar adecuadamente cada valor al diccionario
def database(data,name, price, quant):
    producto={
        "Nombre": name,
        "Precio": price,
        "Cantidad": quant
    }
    for k in producto.items():
        print(k)
    data.append(producto)
    return data

#Apartado para leer el archivo json inicialmente
with open("inventario.json", "r") as file:
    content=json.load(file)
for producto in content["Data"]:
    data_inventario.append(producto)

#Apartado para interfaz
opciones={"Opcion 1": "Agregar Producto", "Opcion 2": "Mostrar Inventario", "Opcion 3": "Buscar", "Opcion 4": "Modificar", "Opcion 5": "Eliminar", "Opcion 6": "Vaciar", "Opcion 7": "Salir"}
while True:
    print("Escoja una opcion")
    print()
    for opt in opciones.items():
        print(opt)
    accion=input()
    if accion!="1" and accion!="2" and accion!="3" and accion!="4" and accion!="5" and accion!="6" and accion!="7":
        print("No ha ingresado una opcion de válida")
    if accion=="1":
        #Apartado para agregar alumnos al archivo json
        product_quant=int(input("¿Cuantos productos desea agregar?: " ))
        for i in range(product_quant):
            prod=input("Ingrese un producto: ").upper()
            while prod.isnumeric():
                prod=input("Ha ingresado un valor no permitido, Ingrese el producto: ").upper()
            price=input("Ingrese su precio: ")
            while not price.isnumeric():
                price=input("Ha ingresado un valor no permitido, Ingrese su precio: ")
            quant=input("Ingrese la cantidad: ")
            while not quant.isnumeric():
                quant=input("Ha ingresado un valor no permitido, Ingrese su cantidad: ")
            database(data_inventario,prod,price,quant)
        base_datos["Data"]=data_inventario
        #Apartado para agregar la base de datos modificada al archivo json
        with open("inventario.json", "w") as file:
            content=json.dump(base_datos, file, indent=2)
    if accion=="2":
        #Apartado para visualizar el archivo json
        with open("inventario.json", "r") as file:
            content=json.load(file)
        for producto in content["Data"]:
            print()
            print("Producto: ", producto["Nombre"])
            print("Precio: ", producto["Precio"])
            print("Cantidad en inventario: ", producto["Cantidad"])
            print()
    if accion=="3":
        #Apartado para visualizar el archivo json
        with open("inventario.json", "r") as file:
            content=json.load(file)
        search=input("Ingrese producto a buscar: ").upper()
        found=False
        for producto in data_inventario:
            if search==producto["Nombre"]:
                found=True
                print()
                print("Se ha encontrado coincidencia:")
                print("Su producto es: ", producto["Nombre"])
                print("Precio: ", producto["Precio"])
                print("Cantidad en inventario: ", producto["Cantidad"])
                break
        if found==False:
            print("No se ha encontrado coincidencia")
    if accion=="4":
        #Apartado para visualizar el archivo json
        with open("inventario.json", "r") as file:
            content=json.load(file)
        search=input("Ingrese producto a modificar: ").upper()
        found=False
        for producto in data_inventario:
            if search==producto["Nombre"]:
                print()
                print("Se ha encontrado coincidencia:")
                print("Su producto es: ", producto["Nombre"])
                print("Precio: ", producto["Precio"])
                print("Cantidad en inventario: ", producto["Cantidad"])
                found=True
                data_inventario.remove(producto)
                prod=search.upper()
                price=input("Ingrese su precio: ")
                while not price.isnumeric():
                    price=input("Ha ingresado un valor no permitido, Ingrese su precio: ")
                quant=input("Ingrese la cantidad: ")
                while not quant.isnumeric():
                    quant=input("Ha ingresado un valor no permitido, Ingrese su cantidad: ")
                database(data_inventario,prod,price,quant)
            else:
                break
            base_datos["Data"]=data_inventario
        if found==False:
            print("No se ha encontrado coincidencia")
        #Apartado para agregar la base de datos modificada al archivo json
        with open("inventario.json", "w") as file:
            content=json.dump(base_datos, file, indent=2)
    if accion=="5":
        #Apartado para visualizar el archivo json
        with open("inventario.json", "r") as file:
            content=json.load(file)
        search=input("Ingrese producto a eliminar: ").upper()
        found=False
        for producto in data_inventario:
            if search==producto["Nombre"]:
                print("Se ha encontrado coincidencia")
                found=True
                data_inventario.remove(producto)
            base_datos["Data"]=data_inventario
            #Apartado para agregar la base de datos modificada al archivo json
            with open("inventario.json", "w") as file:
                content=json.dump(base_datos, file, indent=2)
        if found==False:
            print("No se ha encontrado coincidencia")
    if accion=="6":
        with open("inventario.json", "w") as file:
            base_datos["Data"]=""
            content=json.dump(base_datos, file, indent=2)
    if accion=="7":
        exit("Se ha detenido la simulación")