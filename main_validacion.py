import modulos.intervalos as intervalos
import modulos.cifrado as crypto

#Pruebas lista
print("Inicio prueba de validacion listas")
print("\n")

#valor1=10
#lista1=[2,20,25]
#print("Prueba 0", intervalos.val_int(valor1, lista1))#Respuesta: TypeError

valor1=10
lista1=[2,20]
print("Prueba 1", intervalos.val_int(valor1, lista1))#Respuesta: Verdadero

valor1=25
lista1=[2,4]
print("Prueba 2", intervalos.val_int(valor1, lista1))#Respuesta: Falso

#valor1=10
#lista1=[6,3]
#print("Prueba 3", intervalos.val_int(valor1, lista1))#Respuesta: Falso

#valor1=4
#lista1=[15,3]
#print("Prueba 4", intervalos.val_int(valor1, lista1))#Respuesta: Falso

valor1=2
lista1=[2,20]
print("Prueba 5", intervalos.val_int(valor1, lista1))#Respuesta: Verdadero

#Fin Pruebas Lista

#Puebas Tuplas
print("\n")
print("Inicio prueba de validacion Tuplas")
print("\n")

valor1=10
lista1=(2,12)
print("Prueba 1", intervalos.val_int(valor1, lista1))#Respuesta: Verdadero

valor1=10
lista1=(2,10)
print("Prueba 2", intervalos.val_int(valor1, lista1))#Respuesta: Falso

valor1=2
lista1=(2,10)
print("Prueba 3", intervalos.val_int(valor1, lista1))#Respuesta: Falso

#valor1=5
#lista1=(6,3)
#print("Prueba 4", intervalos.val_int(valor1, lista1))#Respuesta: Falso

#valor1=4
#lista1=(15,3)
#print("Prueba 5", intervalos.val_int(valor1, lista1))#Respuesta: Falso

#Fin Pruebas Tuplas

#Prueba Argumento 1
print("\n")
print("Inicio prueba de validacion argumento 1")
print("\n")

valor1="a"
print("Prueba 1", intervalos.val_int(valor1))#Respuesta: Falso

valor1=2
print("Prueba 2", intervalos.val_int(valor1))#Respuesta: Verdadero

valor1=4.0
print("Prueba 3", intervalos.val_int(valor1))#Respuesta: Falso

#valor1="a"
#lista1=[3,6]
#print("Prueba 4", intervalos.val_int(valor1,lista1))#Respuesta: Falso

#Fin Pruebas Argumento 1


#Prueba Argumentos mayores que 2

print("\n")
print("Inicio prueba de validacion argumento 1")
print("\n")

#valor1=5
#lista1=[2,20]
#tupla1=(6,3)
#print("Prueba 1", intervalos.val_int(valor1,lista1,tupla1))#Respuesta: Falso

#Fin Pruebas Argumentos mayores que 2

#APARTADO PARA PRUEBAS FLOAT

#Pruebas Float
print("Inicio prueba de validacion listas")
print("\n")

valor1=4.5
lista1=[2,20.2]
print("Prueba 1", intervalos.val_float(valor1, lista1))#Respuesta: Verdadero

valor1=2.3
lista1=[2,4]
print("Prueba 2", intervalos.val_float(valor1, lista1))#Respuesta: Falso

valor1=2.3
lista1=[2.3,4.7]
print("Prueba 3", intervalos.val_float(valor1, lista1))#Respuesta: Falso


print("Inicio prueba de validacion Complejos")
print("\n")

valor1=3+4j
print("Prueba 0", intervalos.val_complex(valor1))#Respuesta: True

valor1=3+4j
lista1=[2,28]
print("Prueba 1", intervalos.val_complex(valor1, lista1))#Respuesta: True

valor1=3+4j
lista1=[3+4j,6]
print("Prueba 2", intervalos.val_complex(valor1, lista1))#Respuesta: True

valor1=3+4j
lista1=[3+7j,12]
print("Prueba 3", intervalos.val_complex(valor1, lista1))#Respuesta: Falso

valor1=3+4j
lista1=(3+4j,12)
print("Prueba 4", intervalos.val_complex(valor1, lista1))#Respuesta: Falso

valor1=3+4j
lista1=(3+2j,6+5j)
print("Prueba 5", intervalos.val_complex(valor1, lista1))#Respuesta: Falso

#valor1=3+4j
#lista1=(13+2j,6+5j)
#print("Prueba 5", intervalos.val_complex(valor1, lista1))#Respuesta: ValueError

palabra="Hola mundo"
accion="1"
crypto.codificado(palabra,accion)
accion="2"
crypto.codificado(palabra,accion)
print("\n")

palabra="¿Desea usted aprobar programacion?, Respuesta=Si!"
accion="1"
crypto.codificado(palabra,accion)
accion="2"
crypto.codificado(palabra,accion)
print("\n")

palabra="veinticinco=(25)"
accion="1"
crypto.codificado(palabra,accion)
accion="2"
crypto.codificado(palabra,accion)
print("\n")

#APARTADO PARA PRUEBAS LIST

print("Inicio prueba de validacion listas")
print("\n")

lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]
string="len"
print("Prueba 1", intervalos.val_list(lista1, lista2, string))#Respuesta: True

lista1=[1,2,3,4,5]
lista2=[1,2,3,4,5]
string="value"
print("Prueba 2", intervalos.val_list(lista1, lista2, string))#Respuesta: True

lista1=[1,2,3,4,5]
lista2=[1,2,3,4]
string="value"
print("Prueba 3", intervalos.val_list(lista1, lista2, string))#Respuesta: False

lista1=[5,4,3,2,1]
lista2=[1,2,3,4,5]
string="value"
print("Prueba 4", intervalos.val_list(lista1, lista2, string))#Respuesta: True

lista1=[1]
lista2=1
string="len"
print("Prueba 5", intervalos.val_list(lista1, lista2, string))#Respuesta: True

lista1=[1,2,3,4,5]
lista2=5
string="len"
print("Prueba 6", intervalos.val_list(lista1, lista2, string))#Respuesta: True

lista1=[5]
lista2=5
string="value"
print("Prueba 7", intervalos.val_list(lista1, lista2, string))#Respuesta: False