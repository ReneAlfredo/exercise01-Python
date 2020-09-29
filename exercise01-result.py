# Alumno: René Alfredo Arévalo Ayala
# Carné: 20192110


#   Indicación
"""
cliente:
    quiero escribir un programa python que reciba de input del usuario
    un nombre, un producto, costo
    y se guarde en una lista con diccinarios, el registro es un diccionario
    y va a ser guardado en una lista
programador:
    vaya

cliente:
    mira me gusta pero cada vez que inicio el programa, me borra el cliente anterior
    y solo puedo guardar el que he ingresado en ese momento, no habria forma de
    que se guarde a los 3 clientes que tengo?
programador:
    vaya
mente:
    y pollo no queres?

cliente:
    mira esta buenisimo peeeerroooooo, fijate que mi clientela a aumentado a veces tengo
    3 a veces 5  a veces 10 osea ya no se cuantos clientes tendre en un dia, podrias
    agregarle alguna forma de que yo le diga cuando quiero que se detenga y que me muestre
    el reporte de lo que llevo en costo total hasta ese momento.
programador:
    vaya
mente:
    no te pide nada el gusto mono
"""


# Creamos una lista vacía.
registroClientes = []
# inicializamos dos variables que necesitaremos. 'i' para salir/entrar en los bucles. 'costoSum' para tener el costo total.
i = 0
costoSum = 0.00

# Mientras 'i' no valga 2, el usuario no podrá salir del bucle.
while i != 2:
    print("")
    # Damos la bienvenida al usuario e informamos del costo acumulado.
    print("¡Bienvenido de nuevo! ¡Registremos una nueva compra!")
    print("Actualmente el costo total es de: $" + str(costoSum))
    # pedimos al usuario los datos del cliente.
    cliente = input("Nombre del cliente: ")
    producto = input("Nombre del producto: ")
    costo = float(input("Costo del producto ($0.00): "))

    # sumamos costos para poder informar sobre el costo total.
    costoSum = costoSum + costo

    # guardamos datos en un diccionario.
    registro = {"cliente": cliente, "producto": producto, "costo": costo}
    # enviamos el diccionario a una lista.
    registroClientes.append(registro)

    # preguntamos al usuario si desea continuar.
    print("")
    print("¿Desea agregar otro cliente más? Ingrese el numero de su opción")
    print("1- Ingresar otro cliente")
    print("2- Parar el programa")

    i = int(input())

    # mientras el usuario no ingrese '1' o '2', no podrá salir de este bucle
    while i != 1 and i != 2:
        print("")
        print("Opps! Seleccione una opcion válida")
        print("1- Ingresar otro cliente")
        print("2- Parar el programa")
        i = int(input())

# nos despedimos e informamos del costo total al usuario
print("")
print("¡Gracias por preferirnos!")
print("Sus costos totales son: $" + str(costoSum))