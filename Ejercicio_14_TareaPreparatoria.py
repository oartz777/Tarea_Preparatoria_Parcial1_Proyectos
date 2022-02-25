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

    Ejercicio 14 Modelos de carro

    1) Introducir el modelo y kilometraje
    2) Mostrar Historial
    0) Apagar consola
   
    """)
 
 opcion = int(input("Elige una opción: ") ) 

 if opcion == 1:
        
            modelo=int(input("Introduce el modelo del taxi: "))
            kilometraje=int(input("Introduce el kilometraje del taxi: "))
           

            file = open ("Ejercicio_14_TareaPreparatoria.txt", "a")
            file.write ('modelo= %s'% modelo + '\n')
            file.write ('kilometraje= %s'% kilometraje + '\n')

            if modelo<=2007 and kilometraje>=20001:
                estado="Necesita renovarse"
                print(estado, "\n")
                file.write ('estado= %s'% estado + '\n')
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_14(modelo,kilometraje,condicion) VALUES(%s,%s,%s);",(modelo,kilometraje,estado))
                conexion.commit()
                cursor.close()

            elif modelo>=2006 and modelo<=2013 and kilometraje>=20000:
                estado="Mantenimiento"
                print(estado, "\n")
                file.write ('estado= %s'% estado + '\n')
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_14(modelo,kilometraje,condicion) VALUES(%s,%s,%s);",(modelo,kilometraje,estado))
                conexion.commit()
                cursor.close()

            elif modelo>=2013 and kilometraje<=10000:
                estado="Optimas condiciones"
                print(estado, "\n")
                file.write ('estado= %s'% estado + '\n')
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_14(modelo,kilometraje,condicion) VALUES(%s,%s,%s);",(modelo,kilometraje,estado))
                conexion.commit()
                cursor.close()
    
            else :
                print("Mecanico \n")

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_14(modelo,kilometraje,condicion) VALUES(%s,%s,%s);",(modelo,kilometraje,"Mecanico"))
                conexion.commit()
                cursor.close()
            
 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio_14;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 