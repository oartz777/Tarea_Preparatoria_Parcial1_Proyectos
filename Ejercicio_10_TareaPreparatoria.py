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
    Ejercicio 10 Tipo de triangulos
    
    1) Introducir los valores de los 3 lados del triangulo
    2) Mostrar Historial
    0) Apagar consola
   
    """)
 
 opcion = int(input("Elige una opción: ") ) 

 if opcion == 1:
        
            n1 = float(input("Introduce el valor del primer lado: ") )
            n2 = float(input("Introduce el valor del segundo lado: ") )
            n3 = float(input("Introduce el valor del tercer lado: ") )
        

            file = open ("Ejercicio_10_TareaPreparatoria.txt", "a")
            file.write ('lado 1= %s'% n1 + '\n')
            file.write ('lado 2= %s'% n2 + '\n')
            file.write ('lado 3= %s'% n3 + '\n')

        

            if n1 == n2 and n1 == n3 and n2 == n3:
                tipo="Equilatero"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_10(lado_1,lado_2,lado_3,tipo_de_triangulo) VALUES(%s,%s,%s,%s);",(n1,n2,n3,tipo))
                conexion.commit()
                cursor.close()
            
                
            elif n1 != n2 and n1 != n3 and n2 != n3:
                tipo="Escaleno"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_10(lado_1,lado_2,lado_3,tipo_de_triangulo) VALUES(%s,%s,%s,%s);",(n1,n2,n3,tipo))
                conexion.commit()
                cursor.close()

            elif n1 == n2 and n1 != n3 and n2 != n3:
                tipo="Isosceles"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_10(lado_1,lado_2,lado_3,tipo_de_triangulo) VALUES(%s,%s,%s,%s);",(n1,n2,n3,tipo))
                conexion.commit()
                cursor.close()
            
            elif n1 == n3 and n1 != n2 and n3 != n2:
                tipo="Isosceles"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_10(lado_1,lado_2,lado_3,tipo_de_triangulo) VALUES(%s,%s,%s,%s);",(n1,n2,n3,tipo))
                conexion.commit()
                cursor.close()
                
            elif n2 == n3 and n2 != n1 and n3 != n1:
                tipo="Isosceles"
                print(" ")
                print("RESULTADO:",tipo)
                file.write ('el triangulo es= %s'% tipo + '\n')

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_10(lado_1,lado_2,lado_3,tipo_de_triangulo) VALUES(%s,%s,%s,%s);",(n1,n2,n3,tipo))
                conexion.commit()
                cursor.close() 

 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio_10;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 

