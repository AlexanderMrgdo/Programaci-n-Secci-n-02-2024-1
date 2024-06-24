print("Bienvenido al programa de cifrado de César")
opcion1=("1. Cifrar")
opcion2=("2. Descifrar")
opcion3=("3. Stop")
abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
msg=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
clv_cifrado=int(input("ingrese un numero: "))
print(msg)
msg=msg[(len(msg)-clv_cifrado):]
print(msg)
for letras in abecedario[0:(27-clv_cifrado)]:
    msg.append(letras)
print(msg)
dict_cifrado=dict()
for key in abecedario:
    for value in msg:
        dict_cifrado[key]=value
dict_descifrado=dict()
for key in msg:
    for value in abecedario:
        dict_descifrado[key]=value
for key in dict_cifrado:
    for value in key:
        print({key:value})
        break
preguntas=dict([("Opcion 1", opcion1), ("Opcion 2", opcion2), ("Opcion 3", opcion3)])
for opcion in preguntas:
    print(preguntas[opcion])
while True:
    preguntas=input("Que desea realizar: ")
    if preguntas=="3":
        exit("Ha dejado de cifrar")
    if preguntas=="2":
        print("Su mensaje descifrado es: ")
    if preguntas=="1":
        palabra=input("Ingrese una palabra para cifrar: ")
        palabra=list(palabra)
        mensaje_cifrado=palabra
        print(mensaje_cifrado)