clas=input("ingrese un numero: ")
if int(clas)<0:
    print("el numero es negativo")
elif int(clas)>100:
    print("el numero es mayor que 100")
elif int(clas)%6==0:
    if int(clas)%3==0:
        if int(clas)%2==0:
            print("el numero es divisible por 6")
elif int(clas)%2==0:
    print("el numero es divisible por 2")
elif int(clas)%3==0:
    print("el numero es divisible por 3")
else:
    print("el numero no cumple ninguna condicion especial")