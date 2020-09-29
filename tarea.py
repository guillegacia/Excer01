listaRegistro = []
cliente = 0
costoTotal = 0
nombre = input("ingrese su nombre: ")

maximosClinetes= int(input("ingresa tu cantidad maxima de clientes que quieres ingresar: "))
print("Bienvenido: "+ nombre)
while cliente <=  maximosClinetes*10000:
    
    print("Ingrese los datos siguientes: ")
    clientes = input("Nombre del cliente: ")
    producto = input("Producto comprado: ")
    costo = float(input("Costo ($0.00): "))
    input("""Nesecita seguir ingresado clientes escriba "si", si no escriba "no" """ )
    finalizar = str(input())
    
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    
    cliente =+ 1
    costoTotal += costo

    #costoTotal = costo + costoTotal
    #for costo in listaRegistro:
           # print(costoTotal)

    if finalizar == "no":
         print("El costo total del dia de hoy es de: "+ str(costoTotal))
         break
    
