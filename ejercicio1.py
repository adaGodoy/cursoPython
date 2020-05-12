#tipos de variables
unstr = "esto es una cedena"
unNumeroEntero = 4.5
unFlotante = 4.5
unBooleano = True
#la variable objeto es cuando se tiene una clase y se crea una instancia de dicha clase
#el simbolo de suma(+) tambien sirve para concatenar sea dos cadenas
nombre = "Ada "
apellido = "Godoy"
nombreCompleto = nombre + apellido
print(nombreCompleto)
#IF 
if(unNumeroEntero != unFlotante):
    print("son distintos numeros")
else:
    print("son numeros iguales")

if(type(unNumeroEntero) != type(unFlotante)):
    print("son distinto tipo de datos")
else:
    print("son del mismo tipo")

if(unNumeroEntero>unFlotante):
    print("es mayor", unNumeroEntero)
elif(unNumeroEntero == unFlotante):
    print("son numeros iguales")
else:
    print("es mayor", unFlotante)
        