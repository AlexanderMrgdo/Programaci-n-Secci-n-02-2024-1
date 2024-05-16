cal=input("ingrese un numero: ")
if int(cal)<0:
    print("calificacion invalida")
elif int(cal)>100:
    print("calificacion invalida")
elif int(cal)<50:
    print("insuficiente")
elif int(cal)<70:
    if int(cal)>=50:
        print("suficiente")
elif int(cal)<90:
    if int(cal)>=70:
        print("bueno")
elif int(cal)>=90:
    print("excelente")
elif int(cal)==100:
    print("calificacion perfecta")