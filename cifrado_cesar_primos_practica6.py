abcedario="abcdefghijklmnñopqrstuvwxyz"
abc=list(abcedario)
cba=list(abcedario)
cba.reverse()
abc_cifrado=[]
clave_cifrado=int(7)
for k in range(0,clave_cifrado):
    abc_cifrado+=cba[k]
abc_cifrado.reverse()
for j in range(0,(27-clave_cifrado)):
    abc_cifrado+=abc[j]
#apartado de cifrado.
abc_list={}
for l in range(27):
    abc_list[abc[l]]=cba[l]
abc_list[" "]=" "
cba_list={}
for p in range(27):
    cba_list[cba[p]]=abc[p]
cba_list[" "]=" "
#Tramo de numeros primos
es_primo=True
lista_primos=list()
while len(lista_primos)<27:
    for t in range(2, 150):
        if t==2 or t==3 or t==5:
            es_primo=True
            lista_primos+=[str(t)]
        if t%2!=0 and t%3!=0 and t%5!=0 and not t==2 and not t==3 and not t==5:
            es_primo=True
            lista_primos+=[str(t)]
        if len(lista_primos)==27:
            break
#Diccionario de cifrado primos.
primos_list={}
for primoa in range(27):
    primos_list[abc[primoa]]=lista_primos[primoa]
primos_list[" "]=" "
list_primos={}
for primob in range(27):
    list_primos[lista_primos[primob]]=abc[primob]
list_primos[" "]=" "
#Fin de Diccionario de cifrado primos.
palabra=input("Ingrese una palabra: ").lower()
while palabra.isnumeric():
    palabra=input("No ha ingresado una palabra valida, intente de nuevo: ").lower()
codificar="Codificar"
decodificar="Decodificar"
detener="Detener"
retornar="Retornar"
primos="Primos"
cesar="Caesar"
cifrados={"Cifrado 1": primos, "Cifrado 2": cesar}
opciones={"Opcion 1": codificar, "Opcion 2": decodificar, "Opcion 3": detener, "Opcion 4": retornar}
while True:
    print("Escoja un método de cifrado")
    print("\n")
    for cifr in cifrados.items():
        print(cifr)
    accion_cifrado=input()
    if accion_cifrado!="1" and accion_cifrado!="2":
        print("No ha ingresado una opcion de cifrado valida")
    if accion_cifrado=="1":
        while True:
            print("Escoja una opcion")
            print("\n")
            for opt in opciones.items():
                print(opt)
            accion=input()
            if accion!="1" and accion!="2" and accion!="3" and accion!="4":
                print("No ha ingresado una opcion valida")
            if accion=="1":
                palabra_cifrada=""
                palabra2=palabra
                palabra2=palabra2.split(" ")
                mensaje_cifrado=[]
                palabra2=list(palabra2)
                palabra=list(palabra)
                palabra_cifrada=[]
                palabra_ws=[]
                print(palabra2)
                for letra1 in range(len(palabra2)):
                    for letra2 in range(len(palabra2)):
                        palabra_ws.append(palabra2[letra1][letra2])
                for letra in palabra:
                    palabra_cifrada.append(primos_list[letra])
                for letra in palabra_ws:
                    mensaje_cifrado.append(primos_list[letra])
                    while len(mensaje_cifrado)<2*len(palabra_ws)-1:
                        if primos_list[letra]==" ":
                            mensaje_cifrado.append(" ")
                            break
                        mensaje_cifrado.append("-")
                        break
                print("\n")
                print("Su mensaje Cifrado es: ", end=" ")
                for value in mensaje_cifrado:
                    print(value, end="")
                print("\n")
            if accion=="2":
                palabra_cifrada=list(palabra_cifrada)
                palabra=""
                for letra in palabra_cifrada:
                    palabra+=list_primos[letra]
                print("\n")
                print("Su mensaje Descifrado es: ", palabra)
                print("\n")
            if accion=="3":
                print("\n")
                exit("Se ha Detenido la simulación")
            if accion=="4":
                palabra_cifrada=list(palabra_cifrada)
                palabra=""
                for letra in palabra_cifrada:
                    palabra+=list_primos[letra]
                break
    if accion_cifrado=="2":
        while True:
            print("Escoja una opcion")
            print("\n")
            for opt in opciones.items():
                print(opt)
            accion=input()
            if accion!="1" and accion!="2" and accion!="3" and accion!="4":
                print("No ha ingresado una opcion valida")
            if accion=="1":
                palabra=list(palabra)
                palabra_cifrada=""
                for letra in palabra:
                    palabra_cifrada+=cba_list[letra]
                print("\n")
                print("Su mensaje Cifrado es: ", palabra_cifrada)
                print("\n")
            if accion=="2":
                palabra_cifrada=list(palabra_cifrada)
                palabra=""
                for letra in palabra_cifrada:
                    palabra+=abc_list[letra]
                print("\n")
                print("Su mensaje Descifrado es: ", palabra)
                print("\n")
            if accion=="3":
                exit("Se ha Detenido la simulación")
            if accion=="4":
                palabra_cifrada=list(palabra_cifrada)
                palabra=""
                for letra in palabra_cifrada:
                    palabra+=abc_list[letra]
                break
#Fin de tramo de cifrado cesar.