#Tramo de numeros primosabcedario="abcdefghijklmnñopqrstuvwxyz.,:;*[](){}¿?¡!$%&/\"
def codificado(palabra,accion):
    global primos_list
    global list_primos
    global mensaje_cifrado
    global palabra_cifrada
    abcedario="abcdefghijklmnñopqrstuvwxyz.,:;*[]()}{¿?¡!$%&/=1234567890"
    abc=list(abcedario)
    lista_primos=list()
    while len(lista_primos)<len(abc):
        for t in range(2, 350):
            if t==2 or t==3 or t==5:
                lista_primos+=[str(t)]
            if t%2!=0 and t%3!=0 and t%5!=0 and not t==2 and not t==3 and not t==5:
                lista_primos+=[str(t)]
            if len(lista_primos)==len(abc):
                break
    #Diccionario de cifrado primos.
    primos_list={}
    list_primos={}
    for k in range(len(abc)):
        primos_list[abc[k]]=lista_primos[k]
    primos_list[" "]=" "
    for l in range(len(abc)):
        list_primos[lista_primos[l]]=abc[l]
    list_primos[" "]=" "
    #for t in list_primos.items():
        #print(t)
    #for v in primos_list.items():
        #print(v)
    palabra=palabra.lower()
    while palabra.isnumeric():
        palabra=input("No ha ingresado una palabra valida, intente de nuevo: ").lower()
#Fin de Diccionario de cifrado primos.
    option={"1": "codificar", "2": "decodificar", "3": "detener"}
    while True:
        print("Escoja una opcion")
        print("\n")
        for opt in option.items():
            print(opt)
        if accion!="1" and accion!="2" and accion!="3":
            print("No ha ingresado una opcion valida")
            break
        if accion=="1":
            palabra_cifrada=""
            mensaje_cifrado=[]
            palabra=list(palabra)
            palabra_cifrada=[]
            for letra in palabra:
                palabra_cifrada.append(primos_list[letra])
            for letra in palabra:
                mensaje_cifrado.append(primos_list[letra])
            print("\n")
            print("Su mensaje Cifrado es: ")
            print("-".join(mensaje_cifrado))#Unir cada elemento de la lista con un guión
            return
        if accion=="2":
            palabra_cifrada=list(palabra_cifrada)
            palabra=""
            for letra in palabra_cifrada:
                palabra+=list_primos[letra]
            print("\n")
            print("Su mensaje Descifrado es: ", palabra)
            return 
        if accion=="3":
            print("\n")
            exit("Se ha Detenido la simulación")