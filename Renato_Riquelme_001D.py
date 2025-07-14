productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

def stock_marca(nombre_producto:str):
    for i in productos:
        print(productos[i][0])
        if productos[i][0].lower() == nombre_producto.lower:
            print("!!! PRODUCTO ENCONTRADO")
            marca_encontrada = productos[i]
            marca_encontrada.insert(0,i)
            return marca_encontrada
        
#print(stock_marca("HP"))



def busqueda_precio(p_min:int,p_max:int):
    for i in stock:
        if stock[i][0] >= p_min and stock[i][0] <= p_max:
            print(stock[i])

#busqueda_precio(240000,350000)





def actualizar_precio(modelo:str,p:int):
    producto_encontrado = busqueda_precio(modelo)
    if producto_encontrado != None:
        #print(producto_encontrado)
        for i in stock:
            if i.upper() == producto_encontrado[0].upper():
                stock[i][0] = p
    else:
        print("El producto no se encontro")

#actualizar_precio("HP",387990,12)
#print(stock)



def valida_texto(mensaje_input):
    while True:
        texto = input(mensaje_input)
        if len(texto.strip()) == 0:
            continue
        else:
            return texto
        


#print(valida_texto("Ingrese una opcion: "))



def valida_numero_entero_positivo(msg_input:str):
    while True:
        try:
            numero = int(input(msg_input))
            if numero <= 0:
                print("No se permiten numeros negativos o 0")
                continue
            else:
                return numero
            
        except ValueError:
            print("Solo se pueden ingresar numeros enteros")
            continue


def menu():
    print("**** M E N U ****")
    while True:
     print("1. Stock marca")
     print("2. Busqueda precio")
     print("3. Actualizar precio")
     print("4. Salir")

     try:
         
         opcion = int(input("Ingrese una opcion: "))
     except ValueError:
         print("Solo se permiten valores numericos")


        
     if opcion == 1:
         stock_producto = valida_texto("Ingrese marca a consultar: ")
         
         
                



     elif opcion == 2:
         
         rango_minimo = valida_numero_entero_positivo("Ingrese precio minimo: ")
         rango_maximo = valida_numero_entero_positivo("Ingrese precio maximo: ")

         busqueda_precio(rango_minimo,rango_maximo)

     elif opcion == 3:
         nombre_marca = valida_texto("Ingrese modelo a actualizar: ")
         nuevo_precio = valida_numero_entero_positivo("Ingrese precio nuevo: ")

         actualizar_precio(nombre_marca,nuevo_precio)

     elif opcion == 4:
         break
     else:
         print("Opcion no valida (1 - 4)")
    
menu()




