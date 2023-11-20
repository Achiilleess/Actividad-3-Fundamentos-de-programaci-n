#codigo hecho por aquiles millan
#DECLARAMOS VARIABLES
#esta variable sera el numero que ingrese el usuario
numeroromano: str
numeroromano = ""
#esta variable sera lo que muestre el output del programa
resultado: int = 0
i: int = 1
j: int

#solicitamos el numero que se quiera traducir
numeroromano = str(input("Ingrese numero: ").upper())

#creamos un ciclo que se encargue de leer la caadena caracter poor caracter a ver cual coincide 
for i in range (len(numeroromano)):

    #esta variable sera util mas adelante, pues necesitaremos crear subcadenas que lean desde una posicion antes de i
    j = i - 1

    if numeroromano[i] == "I":
        #las I en romano indican el valor 1, por ende I, II e III pueden interpretarse como sumas de 1
        resultado = resultado + 1
    elif numeroromano[i] == "V":
        #la V representa el valor 5 en romano, por ende cada que aparezca se sumara 5 al numero
        resultado = resultado + 5
        if numeroromano[j:i + 1] == "IV":
            #hay numeros como el 4 u el 9 que en romano no se representan como IIII o VIIII, si no que se muestran como IV e IX, para solucionar es pproblema y evitar que nos de 6 y 11 cada que aparezcan, restaremos el valor que se añada, en este caso es 2
            resultado = resultado - 2
        #a partiir de aqui aplicaremos la misma logica con las distintas letras utilizadas ppara los numeros romanos, mismo metodo de suma y luego restar el valor extra para los numeros como el 4 y el 9
    elif numeroromano[i] == "X":
        resultado = resultado + 10
        if numeroromano[j:i + 1] == "IX":
            resultado = resultado - 2
    elif numeroromano[i] == "L":
        resultado = resultado + 50
        if numeroromano[j:i + 1] == "XL":
            resultado = resultado - 20
    elif numeroromano[i] == "C":
        resultado = resultado + 100
        if numeroromano[j:i + 1] == "XC":
            resultado = resultado - 20
    elif numeroromano[i] == "D":
        resultado = resultado + 500
        if numeroromano[j:i + 1] == "CD":
            resultado = resultado - 200
    elif numeroromano[i] == "M":
        resultado = resultado + 1000
        if numeroromano[j:i + 1] == "CM":
            resultado = resultado - 200
    else:
        #si el usuariio iingresa algo que no sea un numero romano saldra esto
        print("eso no es un numero romano")

#se muestra el resultado
print(resultado)