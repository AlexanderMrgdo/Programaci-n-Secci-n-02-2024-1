def val_arg2_type_intv(types):
    if (type(types)!=list and not type(types)==tuple) or (type(types)!=tuple and not type(types)==list):
        raise TypeError("El SEGUNDO argumento no es de un tipo permitido")
    if type(types[0])!=complex and type(types[1])!=complex:
        if types[0]>types[1]:
            raise ValueError("El SEGUNDO argumento no es un intervalo válido")
    if (type(types[1])!=complex and type(types[0])==complex):
        modulo_intv_inicial=((types[0].real)**(2)+ (types[0].imag)**(2))**(1/2)
        print(modulo_intv_inicial)
        if modulo_intv_inicial>types[1]:
            raise ValueError("El SEGUNDO argumento no es un intervalo válido")
    if (type(types[0])!=complex and type(types[1])==complex):
        modulo_intv_final=((types[1].real)**(2) + (types[1].imag)**(2))**(1/2)
        print(modulo_intv_final)
        if types[0]>modulo_intv_final:
            raise ValueError("El SEGUNDO argumento no es un intervalo válido")
    if (type(types[1])==complex and type(types[0])==complex):
        modulo_intv_inicial=((types[0].real)**(2)+ (types[0].imag)**(2))**(1/2)
        print(modulo_intv_inicial)
        modulo_intv_final=((types[1].real)**(2) + (types[1].imag)**(2))**(1/2)
        print(modulo_intv_final)
        if modulo_intv_inicial>modulo_intv_final:
            raise ValueError("El SEGUNDO argumento no es un intervalo válido")
    if len(types)!=2:
        raise ValueError("El SEGUNDO argumento no es un intervalo válido")
    
def val_int(*args):
    if len(args)==1:
        if type(args[0])!=int:
            return (False)
        if type(args[0])==int:
            return (True)
    if len(args)==2:
        if type(args[0])!=int:
            return (False)
        val_arg2_type_intv(args[1])#Validacion para lista o tupla del argumento 2
        if type(args[1])==list:
            intervalo=[]
            for limites in range(int(args[1][0]),int(args[1][1])+1):
                intervalo.append(limites)
            for i in range(len(intervalo)):
                if args[0]==intervalo[i]:
                    return (True)
            return(False)
        if type(args[1])==tuple:
            if args[1][0]>args[1][1]:
                raise ValueError("El SEGUNDO argumento no es un intervalo válido")
            intervalo=[]
            for limites in range(int(args[1][0]),int(args[1][1])+1):
                intervalo.append(limites)
            for i in range(len(intervalo)):
                if args[0]==intervalo[i] and args[0]!=args[1][0] and args[0]!=args[1][1]:
                    return (True)
            return(False)
    if len(args)>2:
        return(False)

def val_float(*args):
    if len(args)==1:
        if type(args[0])!=float:
            return (False)
        if type(args[0])==float:
            return (True)
    if len(args)==2:
        if type(args[0])!=float:
            return (False)
        val_arg2_type_intv(args[1])#Validacion para lista o tupla del argumento 2
        #convertir a float todos para poder validar el rango
        intervalo_inicial=float(args[1][0])
        intervalo_final=float(args[1][1])
        valor_intermedio=float(args[0])
        #convertir a float todos para poder validar el rango
        if type(args[1])==list:
            if intervalo_inicial<=valor_intermedio and valor_intermedio<=intervalo_final:
                return (True)
            return(False)
        if type(args[1])==tuple:
            if intervalo_inicial<valor_intermedio and valor_intermedio<intervalo_final:
                return (True)
            return(False)
    if len(args)>2:
        return(False)
    
def val_complex(*args):
    if len(args)==1:
        if type(args[0])==complex:
            return (True)
    if len(args)==2:
        if type(args[0])!=complex:
            return (False)
        modulo=((args[0].real)**(2) + (args[0].imag)**(2))**(1/2)
        val_arg2_type_intv(args[1])
        if type(args[1][0])==complex or type(args[1][1])==complex:
            modulo_intv_inicial=((args[1][0].real)**(2)+ (args[1][0].imag)**(2))**(1/2)
            modulo_intv_final=((args[1][1].real)**(2) + (args[1][1].imag)**(2))**(1/2)
            if type(args[1])==list:
                if modulo_intv_inicial<=modulo and modulo<=modulo_intv_final:
                    return (True)
                return(False)
            if type(args[1])==tuple:
                if modulo_intv_inicial<modulo and modulo<modulo_intv_final:
                    return (True)
                return(False)
    if len(args)>2:
        return(False)
    
def val_list(*args):
    if type(args[0])!=list:
        return (False)
    if len(args)==1:
        if type(args[0])==list:
            return (True)
    if len(args)==2:
        raise ValueError("Se necesita 1 ó 3 argumentos")
    if len(args)==3:
        if  ((args[2])=="len"):
            if (len((args[0]))==args[1]):
                return (True)
            if (len((args[0]))!=args[1]):
                return (False)
        if (args[2])=="value":
            if type(args[1])==list:
                #Apartado bubble sort
                for i in range(len(args[0])-1):
                    for j in range(len(args[0])-i-1):
                        if args[0][j] > args[0] [j+1]:
                            args[0][j],args[0][j+1]=args[0][j+1],args[0][j]
                for t in range(len(args[1])-1):
                    for q in range(len(args[1])-t-1):
                        if args[1][q] > args[1] [q+1]:
                            args[1][q],args[1][q+1]=args[1][q+1],args[1][q]
                #Apartado bubble sort
                if len((args[0]))!=len((args[1])):
                    return (False)
                if args[0]==args[1]:
                    return (True)
                else:
                    return (False)
            if type(args[1])!=list:
                return (False)
            return (True)
        elif (args[2]!="len") and not (args[2])=="value":
            raise ValueError("El TERCER argumento no es válido")
        elif (args[2]!="value") and not (args[2])=="len":
            raise ValueError("El TERCER argumento no es válido")
        if len((args[0]))!=len((args[1])):
            return (False)
        if ((args[0]))!=((args[1])):
            return (False)
        return (True)
    if len(args)>3:
        return (False)
