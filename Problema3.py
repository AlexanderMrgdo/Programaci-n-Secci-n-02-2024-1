mensaje=input("Ingrese ua palaba: ")
abecedario="abcdefghijklmnñopqrstuvwxyz"
abc=list(abecedario)
dict_cifrado=dict()
lista_primos=[]
contador=0
for i in range(2,150):
    if contador==27:
        break
    if i%2==0 and not i==2 or i%3==0 and not i==3 or i%5==0 and not i==5:
        print()
    else:
        lista_primos.append(i)
        contador+=1
print(lista_primos)
n=26
for i in abecedario:
    for k in range(0,len(lista_primos)-n):
        dict_cifrado[i]=k
        n-=1
print(dict_cifrado)
cod="Codificar"
dec="Decodificar"
cont="Contar Frecuencia"
ext="Salir"
opciones={"1": cod, "2": dec, "3": cont, "4": ext}
while True:
    for opt in opciones.items():
        print(opt)
    accion=input("Seleccione una opción")
    if accion=="1":
        print("Placeholder")
    if accion=="2":
        print("Placeholder")
    if accion=="3":
        print("Placeholder")
    if accion=="4":
        exit("Se ha detenido la simulación")