#La productora de eventos “Sanchez Producciones”, necesita desarrollar una aplicación que permita controlar 
#la venta de entradas al concierto de “Michael Jackson” que se realizará de forma exclusiva solo para 50 asistentes. 
#El sistema debe permitir las siguientes operaciones, a través de un menú:
#1.	Comprar entradas
#2.	Mostrar ubicaciones disponibles
#3.	Ver listado de asistentes
#4.	Mostrar ganancias totales
#5.	Salir
#Las características de cada operación, se detallan a continuación:
#Comprar entradas: El sistema debe solicitar al usuario la cantidad de entradas a comprar. Esta cantidad fluctúa entre 1 y 2.
#Una vez ingresada la cantidad validada, el sistema debe desplegar en pantalla las ubicaciones que se encuentran disponibles y las vendidas marcadas con una X.


print("Bienvenido al sistema de venta de entradas")
def mostrar_escenario(escenario):
    print("\t\t\t ESCENARIO\n")
    for i in range(0, 50, 10):
        fila = ""
        for j in range(10):
            fila += f"{escenario[i + j]}\t"
        print(fila)
    print("\n")

def comprar_entradas(escenario, ventas):
    precios = {1: 100000, 2: 100000, 3: 100000, 4: 100000, 5: 100000,
               6: 100000, 7: 100000, 8: 100000, 9: 100000, 10: 100000,
               11: 100000, 12: 100000, 13: 100000, 14: 100000, 15: 100000,
               16: 100000, 17: 100000, 18: 100000, 19: 100000, 20: 100000,
               21: 50000, 22: 50000, 23: 50000, 24: 50000, 25: 50000,
               26: 50000, 27: 50000, 28: 50000, 29: 50000, 30: 50000,
               31: 10000, 32: 10000, 33: 10000, 34: 10000, 35: 10000,
               36: 10000, 37: 10000, 38: 10000, 39: 10000, 40: 10000,
               41: 10000, 42: 10000, 43: 10000, 44: 10000, 45: 10000,
               46: 10000, 47: 10000, 48: 10000, 49: 10000, 50: 10000}

    try:
        cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 o 2): "))
        if cantidad < 1 or cantidad > 2:
            print("Cantidad inválida.")
            return
    except ValueError:
        print("Entrada no válida.")
        return

    total_compra = 0
    for _ in range(cantidad):
        mostrar_escenario(escenario)
        try:
            asiento = int(input("Seleccione el número del asiento que desea comprar: "))
            if asiento < 1 or asiento > 50:
                print("Número de asiento inválido.")
                return
        except ValueError:
            print("Entrada no válida.")
            return
        
        if escenario[asiento - 1] == 'X':
            print("El asiento no está disponible.")
            return
        
        escenario[asiento - 1] = 'X'
        precio = precios[asiento]
        run = input("Ingrese el RUN de la persona que ocupará el asiento (sin guión ni puntos): ")
        ventas.append({'asiento': asiento, 'precio': precio, 'run': run})
        total_compra += precio
        print(f"Se ha comprado el asiento {asiento} por ${precio} para el RUN {run}.\n")
    
    total_vendido = sum(venta['precio'] for venta in ventas)
    print(f"Total de la compra actual: ${total_compra}")
    print(f"Total acumulado de ventas: ${total_vendido}\n")

def mostrar_resumen_ventas(ventas):
    print("\t\t\t RESUMEN DE VENTAS\n")
    total_vendido = 0
    for venta in ventas:
        print(f"Asiento: {venta['asiento']}, Precio: ${venta['precio']}, RUN: {venta['run']}")
        total_vendido += venta['precio']
    print(f"\nTotal vendido: ${total_vendido}\n")

def mostrar_total_ventas_y_ruts(ventas):
    total_vendido = sum(venta['precio'] for venta in ventas)
    ruts = [venta['run'] for venta in ventas]
    print(f"\nTotal de ventas realizadas: ${total_vendido}")
    print("RUT de quienes compraron entradas:")
    for run in ruts:
        print(run)
    print("\n")

escenario = []
for i in range(1, 51):
    escenario.append(str(i))
ventas = []

while True:
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Mostrar resumen de ventas")
    print("4. Mostrar total de ventas y RUTs")
    print("5. Salir")
    
    
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        comprar_entradas(escenario, ventas)
    elif opcion == '2':
        mostrar_escenario(escenario)
    elif opcion == '3':
        mostrar_resumen_ventas(ventas)
    elif opcion == '4':
        mostrar_total_ventas_y_ruts(ventas)
    elif opcion == '5':
        print("¡Gracias por utilizar el sistema de ventas!" "milenka constanza aguilar romero , 2024-06-26 20:07:43")
        
        break
    else:
        print("Opción inválida. Por favor, seleccione nuevamente.\n")