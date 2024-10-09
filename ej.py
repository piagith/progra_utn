continuar = "s"

inventario = [ ]

continuar = input("Bienvenidos/as: desea continuar: s/n ")

#funciones
def mostrar_menu(menu:list)-> str:
    menu = print ('''
      menu:
         1. cargar producto/s.
         2. buscar producto.
         3. ordenar inventario.
         4. mostrar producto mas caro.
         5.mostrar producto mas barato.
         6. mostrar productos con precio mayor a 15000.
         7. salir
               ''')
    
    #carga de productos
def cargar_producto (inventario):
   while True:
        nombre_producto = input("ingrese el producto que quiere cargar: ")
        precio_producto = float(input("ingrese el precio del producto: "))
        cantidad_producto = int(input("ingrese la cantidad de productos: "))
        inventario.append([nombre_producto, precio_producto, cantidad_producto])
        print (f"Producto agregado: {nombre_producto}, Precio: {precio_producto}, Cantidad: {cantidad_producto}")
        
        continuar = input("desea ingresar mas productos: s/n ")
        if continuar.lower() != 's':
            break

def buscar_producto(inventario):
    
    producto_buscado = input("ingrese el nombre del producto: ")
    for producto in inventario:
        if producto[0].lower() == producto_buscado.lower():
            cantidad =int(input("cantidad: "))
            if cantidad <= producto[2]:
                producto[2] -= cantidad
                print (f"se encontraron: {cantidad} de '{producto[0]}")
            else:
                print (f"n hay suficientes")
            return
         


def mostrar_productos(inventario : list)-> list:
    vacio = True
    for producto in inventario:
        if producto[2] > 0:
          nombre = producto [0]
          precio = producto[1]
          cantidad = producto[2]

          vacio = False
          print (f"producto: {nombre}, precio:{precio}, cantidad: {cantidad}")
    if vacio :
        print ("el inventario actualmente esta vacio.")
    continuar = input("¿Desea continuar buscando productos? s/n: ")


def ordenar_inventario(inventario):
    if len(inventario) == 0:
        print ("no hay productos en el inventario para ordenar")
        return
    
    n = len(inventario)

    for i in range(n):
        for j in range(0, n-i-1):
            if inventario[j][1] > inventario[j+1][1]:
                inventario[j], inventario[j+1] = inventario[j+1], inventario[j]

    print("inventario ordenado por precio: ")
    for producto in inventario:
        print(f"producto: {producto[0]}, precio: {producto[1]}, cantidad: {producto[2]}")



def producto_mas_caro(inventario):
    
    if len(inventario) == 0:
        print("no hay prod disponibles")
        return
   
    producto_mas_caro = inventario[0]
    for producto in inventario:
           if producto[1] > producto_mas_caro[1]:
               producto_mas_caro = producto

    print (f"producto mas caro: nombre: {producto_mas_caro[0]}, precio: {producto_mas_caro[1]}, cantidad: {producto_mas_caro[2]}")

def producto_mas_barato(inventario):

    if len (inventario) == 0:
        print("no hay prod disponibles") 
        return

    producto_mas_barato = inventario[0]
    for producto in inventario:
        if producto[1] < producto_mas_barato[1]:
            producto_mas_barato = producto

    print (f"producto mas barato: nombre_ {producto_mas_barato[0]}, precio_ {producto_mas_barato[1]}, cantidad: {producto_mas_barato[2]}") 

def productos_15000(inventario: list):
    
    productos_encontrados = False

    print ("producto con precio mayor a 15000")
    for producto in inventario:
        if producto[1] > 15000:
            nombre = producto[0]
            precio = producto[1]
            cantidad = producto[2]
            print(f"producto: {nombre}, precio: {precio}, cantidad: {cantidad}")
            productos_encontrados = True

    productos_encontrados == False and print ("no se encontraron productos con precio")

def salir():
    print("saliendo del sistema.")



while continuar.lower() == "s":
    mostrar_menu(mostrar_menu)
    opcion = input("seleccione una opcion: ")
    
    match opcion :
        case "1":
            print ("agregar productos ")
            cargar_producto(inventario)
        case "2":
            print ("buscar producto ")
            buscar_producto(inventario)
        case "3":
            print ("ordenar inventario ")
            ordenar_inventario(inventario)
        case "4":
            print("mostrar producto mas caro.")
            producto_mas_caro(inventario)
        case"5":
            print("producto mas barato.")
            producto_mas_barato(inventario)
        case "6":
            print ("mostrar producto con precio mayor a 15000.")
            productos_15000(inventario)
        case "7":
            print("salir del sistema")
            break
        case _:
            print("opcion invalida, seleccione otra por favor")
            
    continuar = input("desea continuar s/n: ")

    #fin programa