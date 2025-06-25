totem = [
    {   "nombre": "Renato", 
        "entrada": "G",
        "codigo": "fortificador1"
    },
    {
        "nombre": "Carlos", 
        "entrada": "CV",
        "codigo": "ilumidaor1"
       

    }




]

def codigo_valido(codigo):
    letras_numeros = "abcdefghijklmñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789"
    for letra in codigo:
        if letra not in letras_numeros:
         return False
    return True


def datos_validos(nombre,entrada,codigo):
   
   for comprador in totem:
      if comprador["nombre"].lower() == nombre.lower():
         print("YA EXISTE EL NOMBRE")
         return False
      
      if entrada.upper() != "G" and entrada.upper() != "V":
         print("DEBE SER G O V")
         return False
      
      if  entrada.upper() != "CV" and entrada.upper() != "PAL":
         print("DEBE SER CV O PAL")
         return False
      
      
      if len(codigo) != 6:
        print("DEBE CONTENER AL MENOS 6 CARACTERES")
        return False
      
      if not codigo_valido(codigo):
         print("LETRAS Y NUMEROS")
         return False
       
      for comprador in totem:
         if comprador["codigo"] == codigo:
            print("YA EXISTE")
            return False
         

def registar_entrada_fortificados():
   print("*** REGISTRO DE ENTRADA***")
   nombre = input("Ingrese su nombre: ")
   entrada = input("Ingrese tipo de entrada (G/V): ")
   codigo = input("Ingrese el codigo de confirmacion: ")


   if datos_validos(nombre,entrada,codigo):
      comprador = {
         "nombre": nombre,
         "entrada":entrada.upper(),
         "codigo": codigo
        }
      totem.append(comprador)
      print("ENTRADA REGISTRADA CON EXITO")



def registar_entrada_iluminados():
   print("*** REGISTRO DE ENTRADA***")
   nombre = input("Ingrese su nombre: ")
   entrada = input("Ingrese tipo de entrada (CV/PAL): ")
   codigo = input("Ingrese el codigo de confirmacion: ")


   if datos_validos(nombre,entrada,codigo):
      comprador = {
         "nombre": nombre,
         "entrada":entrada.upper(),
         "codigo": codigo
        }
      totem.append(comprador)
      print("ENTRADA REGISTRADA CON EXITO")



   

         


def mostrar_stock():
   print("*** STOCK ***")
 
   

      
         


def menu():
   while True:
      print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
      print("1.- Comprar entrada a los Fortidicados")
      print("2.- Comprar entrada a los Iluminados")      
      print("3.- Stock de entradas para ambos conciertos")
      print("4.- Salir")

      opcion = input("ELIGE UN OPCION (1 A 4): ")


      if opcion == "1":
            registar_entrada_fortificados()
      elif  opcion == "2":
         registar_entrada_iluminados()
      elif opcion == "3":
        mostrar_stock()

      elif opcion == "4":
         print("Programa terminado....")
         break
      else:
         print("Opcion no valida")

         
    
         

    
         
    
     







menu ()
      



         

