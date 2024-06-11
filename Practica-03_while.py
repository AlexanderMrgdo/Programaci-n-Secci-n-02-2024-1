num_primo=input("ingrese la cantidad de numeros primos que usted desee, escriba 'stop' para deja de emular numeros ")
lista_primos=[]
sumatoria_primos=[]#Lista para anexar cada potencia al cuadrado de aquellos numeros que sean primos.
es_primo=True
num_primo=int()
for i in range(2, num_primo):
    if i%2==0 or i%3==0 or i%5==0:
        es_primo=False
    while (i==True):
        lista_primos.append(num_primo)
        input("Ingrese un numero mas: ")
    if num_primo=="stop":
        print("Se ha detenido la emulación.")
        break