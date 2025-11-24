from servicios import leer_productos, guardar_productos
import csv


def Agregar_csv():
    print('Agregar productos desde CSV')
    nombre_archivo = input('Ingrese el nombre del archivo CSV (con .csv): ')

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            productos = leer_productos()
            ultimo_id = productos[-1]['id'] if productos else 0

            for fila in lector_csv:
                ultimo_id += 1
                nuevo_producto = {
                    'id': ultimo_id,
                    'nombre': fila['nombre'],
                    'precio': float(fila['precio']),
                    'cantidad': int(fila['cantidad']),
                }
                productos.append(nuevo_producto)

            guardar_productos(productos)
            print('Productos agregados desde el archivo CSV correctamente.')

    except FileNotFoundError:
        print('El archivo no fue encontrado. Por favor, verifique el nombre e intente nuevamente.')
    except KeyError:
        print('El archivo CSV no tiene el formato correcto. Asegúrese de que las columnas sean: nombre, precio, cantidad.')
    except Exception as e:
        print(f'Ocurrió un error al procesar el archivo CSV: {e}')


def cargar_csv():
    print('Cargar productos desde CSV')
    nombre_archivo = input('Ingrese el nombre del archivo CSV (con .csv): ')

    try:
        with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            productos = []

            for fila in lector_csv:
                nuevo_producto = {
                    'id': int(fila['id']),
                    'nombre': fila['nombre'],
                    'precio': float(fila['precio']),
                    'cantidad': int(fila['cantidad']),
                }
                productos.append(nuevo_producto)

            guardar_productos(productos)
            print('Productos cargados desde el archivo CSV correctamente.')
    except:
        return