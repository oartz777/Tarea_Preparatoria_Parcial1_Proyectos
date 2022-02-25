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
    Ejercicio 11 Promedio
    
    1) Introducir los valores de las 3 notas
    2) Mostrar Historial de las notas
    0) Apagar consola
   
    """)
 
 opcion = int(input("Elige una opción: ") ) 

 if opcion == 1:
        
            n1 = int(input("nota 1: ") )
            n2 = int(input("nota 2: ") )
            n3 = int(input("nota 3: ") )
            promedio=(n1+n2+n3)/3
            

            file = open ("Ejercicio_11_TareaPreparatoria.txt", "a")
            file.write ('nota 1= %s'% n1 + '\n')
            file.write ('nota 2= %s'% n2 + '\n')
            file.write ('nota 3= %s'% n3 + '\n')


            if promedio > 60:
                estado="APROBADO"
                print(" ")
                print("RESULTADO:", promedio, estado)
                file.write ('estado= %s'% estado + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_11(nota_1,nota_2,nota_3,estado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,estado))
                conexion.commit()
                cursor.close()
            
                
            elif promedio < 60:
                estado="REPROBADO"
                print(" ")
                print("RESULTADO:",promedio, estado)
                file.write ('estado= %s'% estado + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_11(nota_1,nota_2,nota_3,estado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,estado))
                conexion.commit()
                cursor.close()  

 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio_11;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 