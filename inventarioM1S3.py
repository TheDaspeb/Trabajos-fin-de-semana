import json
import os
import csv

lista = 'productos.json'

# ---------------------------
# LEER DATOS
# ---------------------------

def leer_productos():
    if not os.path.exists(lista):
        return []

    try:
        with open(lista, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

# ---------------------------
# GUARDAR DATOS
# ---------------------------

def guardar_productos(lista):
    with open(lista, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

# ---------------------------
# CREAR PRODUCTO
# ---------------------------

def agregar_producto():#primer funcion añadir productos. 
    #agregar producto al inventario
    print('------Agrega un producto------')

    productos = leer_productos()

    while True:
        nombre = input('Ingrese el nombre del producto: ').lower()
        
        if all(c.isalnum() or c == " " for c in nombre): #Con esto podemos determinar si la palabra tienes caracter especial 
    
            if any(t in nombre for t in "áéíóú"):
                print('No se permiten tildes')
            else:
                break
        else:
            print('No se permiten caracteres especiales.')

    while True:

        try:
            precio = float(input('Ingresa el valor del producto: '))
            if precio >0:
                print('El precio fue ingresado')
                break
            else:
                print('Deben ser número positivos')
        except ValueError:
            print('Ingresa valores númericos')

    while True:
        try:
            cantidad = int(input('Ingresa la cantidad del producto: '))
            if cantidad >0:
                print('Cantidad ingresada Correctamente.')
                break
            else:
                print('Ingrese valores números positivos ')
        except ValueError:
            print('Ingrese números. ')

    nuevo_id = 1 if not productos else productos[-1]["id"] + 1

    nuevo ={
        'ID': nuevo_id,
        'Nombre': nombre,
        'Precio': precio,
        'Cantidad': cantidad,
    }
    productos.append(nuevo)
    guardar_productos(productos)

    print('Producto agregado correctamente. ')

# ---------------------------
# MOSTRAR PRODUCTO
# ---------------------------

def mostrar():

    print('------Agrega un producto------')
    productos = leer_productos()

    if not productos:
        print("\nNo hay productos registrados.\n")
        return

    print("\n LISTA DE PRODUCTOS: ")
    for i in productos:
        print(f"ID: {i['id']} | Nombre: {i['nombre']} | Precio: {i['precio']}   | Cantidad: {i['cantidad']}")
    print()