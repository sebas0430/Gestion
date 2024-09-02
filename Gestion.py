class ProductoCompra:
    def __init__(self, id, nombre, precioCompra, cantidad):
        self.id = id
        self.nombre = nombre
        self.precioCompra = precioCompra
        self.cantidad = cantidad

    def imprimir(self):
        return f'ID: {self.id} \n NOMBRE: {self.nombre} \n PRECIO: {self.precioCompra}$ \n CANTIDAD: {self.cantidad}'


class ProductoVenta:
    def __init__(self, id, nombre, precioVenta):
        self.id = id
        self.nombre = nombre
        self.precioVenta = precioVenta

    def imprimir(self):
        return f'ID: {self.id} \n NOMBRE: {self.nombre} \n PRECIO: {self.precioVenta}$'


productos = []
productosVenta = []
TotalGastos = 0
TotalVentas = 0

def CompraProductoNuevo(id, nombre, precioCompra, cantidad):
    global TotalGastos
    pro = ProductoCompra(id, nombre, precioCompra, cantidad)
    productos.append(pro)
    TotalGastos += precioCompra * cantidad  # Actualizar TotalGastos correctamente
    print("Ya fue agregado el producto")


def CompraProductoAntiguo(id, cantidad):
    global TotalGastos
    for producto in productos:
        if producto.id == id:
            producto.cantidad += cantidad
            TotalGastos += cantidad * producto.precioCompra  # Actualizar TotalGastos
            print("Producto actualizado con más cantidad.")
            return
    print("No se encontró el producto.")


def AsignarPrecioVenta(id, precioVenta):
    for producto in productos:
        if producto.id == id:
            nombre = producto.nombre
            proV = ProductoVenta(id, nombre, precioVenta)
            productosVenta.append(proV)
            print("Precio de venta asignado.")
            return
    print("No se encontró el producto para asignar precio de venta.")


def VentaProducto():
    global TotalVentas
    if not productos:
        print("No hay productos disponibles para la venta.")
        return    
 
    print("Productos disponibles:")
    VerProductosVenta(productosVenta)
    idVenta = int(input("Ingrese el ID del producto que desea adquirir: "))
    for producto in productos:
        cantidadVenta = int(input(f"Ingrese la cantidad a vender de {producto.nombre}: "))
        if cantidadVenta <= producto.cantidad:
                # Verificar si hay un precio de venta asignado
                for productoV in productosVenta:
                    if productoV.id == idVenta:
                        # Calcular la venta y actualizar cantidades
                        producto.cantidad -= cantidadVenta
                        ventaTotal = cantidadVenta * productoV.precioVenta
                        TotalVentas += ventaTotal
                        print(f"Venta realizada. Total: {ventaTotal}$")
                        return
                print("No se ha asignado un precio de venta a este producto.")
                return
        else:
                print(f"No hay suficiente cantidad disponible. Cantidad actual: {producto.cantidad}")
                return
    print("No se encontró el producto para la venta.")


def VerProductos(productos):
    for producto in productos:
        print(producto.imprimir())


def VerProductosVenta(productosVenta):
    for producto in productosVenta:
        print(producto.imprimir())


# Menú de opciones
opc = 1
while opc != "0":
    print("1. Compra Producto")
    print("2. Asignar Precios de venta")
    print("3. Venta Producto")
    print("4. Ver Productos Disponibles")
    print("5. Ver Productos a la venta")
    print("6. Info de ventas")
    print("7. Agregar Costos Extra")
    print("8. IA recomendaciones")
    print("0. SALIR")
    opc = input('Ingrese una opción: ')

    if opc == "1":
        estado = input("El producto es nuevo o quiere más cantidad (nuevo/cantidad): ")
        if estado == "nuevo":
            id = int(input("Ingrese el id: "))
            nombre = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio de compra: "))
            cantidad = int(input("Ingrese la cantidad: "))
            CompraProductoNuevo(id, nombre, precio, cantidad)
        elif estado == "cantidad":
            VerProductos(productos)
            id = int(input("Ingrese el id: "))
            cantidad = int(input("Ingrese la cantidad: "))
            CompraProductoAntiguo(id, cantidad)
        else:
            print("Valor no válido")

    elif opc == "2":
        VerProductos(productos)
        idproducto = int(input("Ingrese el id del producto que desea agregarle un precio de venta: "))
        precioVenta = float(input("Ingrese el precio que desea asignarle: "))
        AsignarPrecioVenta(idproducto, precioVenta)

    elif opc == "3":
        VentaProducto()
    elif opc == "4":
        VerProductos(productos)

    elif opc == "5":
        VerProductosVenta(productosVenta)

    elif opc == "6":
        print(f"Total de gastos en compras: {TotalGastos}$")
        print(f'Total de Ventas {TotalVentas}$')
        print("---------------------------------------------")
        print(f'Balance final: {TotalVentas - TotalGastos }')

    elif opc == "7":
        extra = float(input("Ingrese el costo extra que desea agregar: "))
        TotalGastos += extra
        print("Costo extra agregado.")
    elif opc == "0":
        print("Salida exitosa")

    else:
        print("Opción no válida.")
