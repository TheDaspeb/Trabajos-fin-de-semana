#le pedimos a usuario que ingrese el prodicto, precio y cantidad 
while True:
    nombreP= input('Ingresar el nombre del producto: ').lower()
    if all(c.isalpha() or c == " " for c in nombreP): #Con esto podemos determinar si la palabra tienes caracter especial 
    
        if any(t in nombreP for t in "áéíóúÁÉÍÓÚ"):
            print('No se permiten tildes')
        else:
            print()
            break
    else:
        print('No se permiten caracteres especiales.')

#de debe crear un bucle seguido de condicionales para que el bucle pueda tener un fin. 

while True: 
    precioP=float(input('ingresa el precio del producto: '))

    if precioP>0: #con esta condición si el usuario ingresa número negativos lo volvera a pedir hasta que el número sea valido
        print()
        break
    else:
        print('precio invalido')
    

while True: 
    cantidadP=int(input('ingresa la cantidad del producto: '))

    if cantidadP>0: #aplica lo mismo que en la condicion de arriba 
        print()
        break
    else:
        print('cantidad invalido')

#despues de que el usuario haya ingresado el todo de debe de calcular el precio por la cantidad del producto

costo_total= precioP * cantidadP

#se le indica al usuario de manera detallada de lo que él ingreso y el precio total. 

print(f'El producto ingresado fue: {nombreP} el precio indicado es de: {precioP} y la cantidad ingresado es: {cantidadP} el  costo total es: {costo_total:.2f}')