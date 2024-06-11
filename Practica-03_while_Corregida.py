#Definición de variables.
lista_primos=[]#Lista para anexar cada numero que sea primo.
sumatoria_primos=[]#Lista para anexar cada potencia al cuadrado de aquellos numeros que sean primos.
es_primo=True#Condicion inicialmente verdadera.
n=str()#variable definida
#Definición de variables.

#Bucle continuo hasta que se cancele mediante el usuario.
while True:#Bucle para continuar agregando numeros hasta que el usuario lo detenga mediante la palabra "stop"
    n=input("ingrese un numero primo: ") #Interfaz del usuario.
    if n=="stop":#Condicion de finalizado mediante el str "stop"
        es_primo=False
        print("se ha detenido la simulación")
        print("se han encontrado estos: ", lista_primos, "numeros primos entre los valores ingresados")
        print("la sumatoria es:", sum(sumatoria_primos))
        exit()
    while (not n.isnumeric()): #Puerta de acceso al codigo.
        n=input("El dato ingresado no es un número válido. Ingrese un numero: ") #Tienes otro reintento.
        if n.isnumeric():#Ingresaste un valor numerico, puedes continuar.
            break
        if n=="stop":
            print("se ha detenido la simulación")
            print("se han encontrado estos: ", lista_primos, "numeros primos entre los valores ingresados")
            print("la sumatoria es:", sum(sumatoria_primos))
            exit("se ha detenido la simulación")
    n=int(n)#Transforma en entero la variable "n".
    for i in range(2, n+1):#Iterado que verifica entre un rango desde 2 hasta n+1 cuales son primos.
        for j in range(2, i):#Verifica si el numero es primo continuamente verificando el residuo entre cada numero del iterado anterior.
            if i%j==0 or i%2==0 and not i==2 or i%3==0 and not i==3 or i%5==0 and not i==5:#Verificar si i dividido entre j su residuo es 0, o si es divisible entre los factores 2,3,5. Excluyendo al 2, 3 y 5.
                es_primo=False
                break
            if i%j!=0:#Apartado para verificar si el numero en el iterado "i" es primo verificando el residuo entre cada numero iterado anteriormente.
                es_primo=True
    if es_primo==True:#Se ha confirmado que el numero es primo, agregalo a la lista.
        print("Se ha añadido", n, "a la lista")     
        sumatoria_primos.append(n*n)
        lista_primos.append(n)
    if es_primo==False:
        print("Se ha ingresado un numero no primo,", n, "intente con otro valor")