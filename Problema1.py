while True:
    palabra=input("Ingrese una palabra: ")
    palabra=list(palabra)
    palabra_reverse=list(palabra)
    palabra_reverse.reverse()
    if palabra==palabra_reverse:
        print("La palabra es un palíndromo")
        break
    else:
        print("La palabra no es un palíndromo")