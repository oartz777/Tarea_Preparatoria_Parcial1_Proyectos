import psycopg2


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
    Ejercicio 13 Año Bisiesto
    
    1) Introducir el año de nacimiento
    2) Mostrar Historial de las notas
    0) Apagar consola
   
    """)
 
 opcion = int(input("Elige una opción: ") ) 

 if opcion == 1:
        
            year = int(input("introduce tu año de nacimiento:"))
            file = open ("Ejercicio_13_TareaPreparatoria.txt", "a")
            file.write ('año de nacimiento= %s'% year + '\n')


            if year % 4 != 0:
                print("No es bisiesto")
                year_1 = "No es bisiesto"
                print(" ")
                print("RESULTADO:", year, year_1)
                file.write ('el año es= %s'% year_1 + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_13(year,year_1) VALUES(%s,%s);",(year,year_1))
                conexion.commit()
                cursor.close()
            
                
            elif year % 4 == 0 and year % 100 != 0:
                print("Bisiesto")
                year_1 = "Bisiesto"
                print(" ")
                print("RESULTADO:", year, year_1)
                file.write ('el año es= %s'% year_1 + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_13(year,year_1) VALUES(%s,%s);",(year,year_1))
                conexion.commit()
                cursor.close()

            elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
                print(" No es bisiesto")
                year_1 = "No es bisiesto"
                print(" ")
                print("RESULTADO:", year, year_1)
                file.write ('el año es= %s'% year_1 + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_13(year,year_1) VALUES(%s,%s);",(year,year_1))
                conexion.commit()
                cursor.close()

            elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                print("Bisiesto")
                year_1 = "Bisiesto"
                print(" ")
                print("RESULTADO:", year, year_1)
                file.write ('el año es= %s'% year_1 + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_13(year,year_1) VALUES(%s,%s);",(year,year_1))
                conexion.commit()
                cursor.close()



 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio_13;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 