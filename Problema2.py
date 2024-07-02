palabra=input("Ingrese una palabra: ")
palabra2=input("Ingrese otra palabra: ")
palabra=list(palabra)
palabra2=list(palabra2)
for i in range(len(palabra)-1):
    for j in range(len(palabra)-i-1):
        if palabra[j] > palabra [j+1]:
            palabra[j],palabra[j+1]=palabra[j+1],palabra[j]
            print(palabra)
for t in range(len(palabra2)-1):
    for q in range(len(palabra2)-t-1):
        if palabra2[q] > palabra2 [q+1]:
            palabra2[q],palabra2[q+1]=palabra2[q+1],palabra2[q]
            print(palabra2)
if palabra==palabra2:
    print("La palabra es un Anagrama")
else:
    print("La palabra no es un Anagrama")