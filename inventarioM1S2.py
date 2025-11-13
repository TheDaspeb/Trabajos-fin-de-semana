inventario = []

def agregar_producto():#primer funcion añadir productos. 
    #agregar producto al inventario
    print('------Agrega un producto----')

    while True:
        nombre = input('Ingrese el nombre del producto: ')
        
        if all(c.isalnum() or c == " " for c in nombre): #Con esto podemos determinar si la palabra tienes caracter especial 
    
            if any(t in nombre for t in "áéíóú"):
                print('No se permiten tildes')
            else:
                break
        else:
            print('No se permiten caracteres especiales.')
    
    #se debe crear un bucle para que el usuario pueda ingresar solo números

    while True:
        try:
            precio = float(input('Ingresa el precio del producto: '))
            if precio > 0:
                print('Precio agregado.')
                break
            else:
                print('Precio inválido. Debe ser mayor a 0.')
        except ValueError:
            print('¡Inválido! Por favor ingresa un número.')

# Validar cantidad
    while True:
        try:
            cantidad = int(input('Ingresa la cantidad del producto: '))
            if cantidad > 0:
                print('Cantidad agregada')
                break
            else:
                print('Cantidad inválida. Debe ser mayor a 0.')
        except ValueError:
            print('¡Inválido! Por favor ingresa un número entero.')
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
    }
    inventario.append(producto)
    print(f'El producto {nombre} se agrego correctamente.')
    
def Mostrar_inventario():
    #mostrará todos los productos agregados a la lista invetario
    print('Mostrar inventario')

    if not inventario:# si desde el principio el usuario quere ver los producto no le dejará
        print('El inventario esta vacío.')
        return
    
    for producto in inventario:# acá le mostrará todo, lo que se ingresó
        print(f'Producto: {producto['nombre']}    |   El precio es: {producto['precio']}    |   la cantidad es: {producto['cantidad']}')
        print('--------------')

def calcular_estadistica():
    print('Calcular estadistica')

    if not inventario:#con esto no se calculara nada si el inventario esta vacio.
        print('No hay productos para carcular la estadística. ')
        return
    
    valor_total = 0
    Cantidad_total = 0

    for producto in inventario:
        valor_total += producto['precio'] * producto['cantidad']
        Cantidad_total += producto['cantidad']

    print(f'Valor total del inventario: {valor_total:.2f}')
    print(f'Cantidad de unidades: {Cantidad_total}')
    print(f'Número de productos diferentes: {len(inventario)}')

def menu():

    while True:
        print('      *Bienvenido*      ')

        try:
            opcion = int(input('ingresa un número de 1 al 4\nEstas son nuestras opciones:\n1. Agregar productos\n2. Mostrar productos\n3. calcular estadística\n4. salir\n Cual elijes: '))
        except ValueError:
            print('Opcion invalida, por favor ingrese valores numéricos')
            continue

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            Mostrar_inventario()
        elif opcion == 3:
            calcular_estadistica()
        elif opcion == 4:
            print('Saliste del programa')
            break
        else:
            print('Opción no valida')

menu()