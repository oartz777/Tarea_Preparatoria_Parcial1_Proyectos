import psycopg2
import math


def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, ingrese un número")  
    return numero

try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "victor",
        password = "victor",
        dbname = "postgres"
    )
    print("conexión exitosa")
except psycopg2.Error as e:
    print("Ocurrio un error en la conexion")
    print("Verifique los parametros")


while True:
 print("""
    Ejercicio 12 Numeros divisibles entre 7
    
    1) Introducir los valores de las 3 notas
    2) Mostrar Historial
    0) Apagar consola
   
    """)
 
 opcion = int(input("Elige una opción: ") ) 

 if opcion == 1:
        
           n1 = int(input("Ingrese un numero:"))
           n2 = 7
           residuo = n1%n2

           file = open ("Ejercicio_12_TareaPreparatoria.txt", "a")
           file.write ('numero_1= %s'% n1 + '\n')

           if residuo == 0:
               divisible= "SI"
               factorial = math.factorial(n1)

               print("el numero",n1,"SI es divisible entre",n2)
               print("El factorial del numero es:",factorial)

               file.write ('es divisible entre 7?: %s'% divisible  + '\n')
               file.write ('factorial: %s'% factorial  + '\n')

               cursor = conexion.cursor()
               cursor.execute("INSERT INTO ejercicio_12(numero,divisible_entre_7,factorial) VALUES(%s,%s,%s);",(n1,divisible,factorial))
               conexion.commit()
               cursor.close() 

           elif residuo !=0:
               divisible= "NO"
               no_factorial=0 
               print("el numero",n1,"NO es divisible entre",n2)

               file.write ('es divisible entre 7?: %s'% divisible  + '\n')

               cursor = conexion.cursor()
               cursor.execute("INSERT INTO ejercicio_12(numero,divisible_entre_7,factorial) VALUES(%s,%s,%s);",(n1,divisible,no_factorial))
               conexion.commit()
               cursor.close()    

           
 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio_12;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 




  
