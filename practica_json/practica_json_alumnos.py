import json
data_alumnos=[]
base_datos={}

#Funcion para asignar adecuadamente cada valor al diccionario
def database(data,name, age, sem):
    alumno={
        "Nombre": name,
        "Edad": age,
        "Semestre": sem
    }
    for k in alumno.items():
        print(k)
    data.append(alumno)
    return data

#Apartado para leer el archivo json inicialmente
with open("alumnos.json", "r") as file:
    content=json.load(file)
for estudiante in content["Data"]:
    data_alumnos.append(estudiante)

#Apartado para interfaz
opciones={"Opcion 1": "Agregar", "Opcion 2": "Leer", "Opcion 3": "Vaciar", "Opcion 4": "Salir"}
while True:
    print("Escoja una opcion")
    for opt in opciones.items():
        print(opt)
    accion=input()
    if accion!="1" and accion!="2" and accion!="3" and accion!="4":
        print("No ha ingresado una opcion de válida")
    if accion=="1":
        #Apartado para agregar alumnos al archivo json
        alum_quant=int(input("¿Cuantos estudiantes desea agregar?: " ))
        for i in range(alum_quant):
            alum=input("Ingrese un estudiante: ")
            edad=input("Ingrese su edad: ")
            semester=input("Ingrese el semestre en curso: ")
            database(data_alumnos,alum,edad,semester)
        base_datos["Data"]=data_alumnos
        #Apartado para agregar la base de datos modificada al archivo json
        with open("alumnos.json", "w") as file:
            content=json.dump(base_datos, file, indent=2)
    if accion=="2":
        #Apartado para visualizar el archivo json
        with open("alumnos.json", "r") as file:
            content=json.load(file)
        for estudiante in content["Data"]:
            print(estudiante)
    if accion=="3":
        with open("alumnos.json", "w") as file:
            base_datos["Data"]=""
            content=json.dump(base_datos, file, indent=2)
    if accion=="4":
        exit("Se ha detenido la simulación")