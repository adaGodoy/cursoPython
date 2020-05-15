cadena = """ Menu principal\n
            1. sumar dos elementos\n
            2. restar dos elementos\n
            3. crear una cadena\n
            4. salir
        """#esta va ser un cadena con saltos de linea inlcuidos sin afectar el programa
print(cadena)
centinela = 101# se le dio un valor para que mientras se cumpla en la condicion de while recorrera el programa
intentos = 0 #en esta variable se da el numero de intentos donde el usuario puede equivocarse
while(centinela == 101 and intentos < 3):# aca va ingresar solo si se cumple el valor que se le dio a la variable
    respuesta = input("ingrese una de las opciones: ")# input es para pedirle datos al usuario mediante un msj preestablecido

    try:#inicia un encapsulamiento para excepciones
        respuesta = int(respuesta)# se convierte de cadena a valor entero para la eleccion del usuario y comprobacion de la excepcion
        if(respuesta == 1):
            num1 = int(input("ingrese el primer valor: "))
            num2 = int(input("ingrese el segundo valor: "))
            suma = num1 + num2
            print(num1, " + ", num2, "=", suma)
        elif(respuesta == 2):
            num1 = int(input("ingrese el primer valor: "))
            num2 = int(input("ingrese el segundo valor: "))
            resta = num1 - num2
            print(num1, " - ", num2, "=", resta)
        elif(respuesta == 3):
            cadenaNueva = input("Ingrese su cadena de texto: ")
            print(cadenaNueva)
        elif(respuesta == 4):#opcion de salida del programa
            print("gracias, hasta la proxima")
            centinela = 1000# sobreescribe el valor de la variable para el momento de volver al recorrer el programa ya no sea verdadera la comprobacion
        else:# cuando el usuario ingrese algo que no se le solicita en el menu
            print("Ingreso un valor que no se encuentra en el menu")
    except ValueError:# la palabra reservada de ValueError es para que se pueda cumplir la excepcion sobre lo que el programa no va aceptar
        # esto lo reconocieria como un error y le dira al usuario con un msj que esta mal lo que ingresa
        print("ingreso una letra")
        intentos += 1# esta se convierte en una variable acumuladora y cada que el usuario cometa un error ira aumentando
        # al pasar eso en el while se le dio una comparacion, si esta deja de cumplirse el programa dejara de recorrerse
        # y saldra del programa