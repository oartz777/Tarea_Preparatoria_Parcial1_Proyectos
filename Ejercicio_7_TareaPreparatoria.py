import psycopg2
 
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


def input_numero(msj=" "):
    numero =0
    while True:
        try:
            numero=int(input(msj))
            break
        except ValueError:
            print("Error, ingrese un número")  
    return numero

while True:
 print("""
    Ejercicio 7 Suma de 0 al numero que ingrese
    
    1) Introducir numero
    2) Mostrar Historial
    0) Apagar consola
   
    """)
 
 opcion = int(input("Elige una opción: ") ) 

 if opcion == 1:
        
        n1= input_numero("Ingrese un numero: ")
        suma = sum(range(1, n1+1))
        print(suma)

        file = open ("Ejercicio_7_TareaPreparatoria.txt", "a")
        file.write ('Numero ingresado= %s'% n1  + '\n')
        file.write ('Suma= %s'% suma  + '\n')

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ejercicio_7(numero_ingresado,suma) VALUES(%s,%s);",(n1,suma))
        conexion.commit()
        cursor.close()

 elif opcion == 2:  

            cursor = conexion.cursor()
            SQL = 'SELECT*FROM ejercicio_7;'
            cursor.execute(SQL)
            valores = cursor.fetchall()
            print(valores)
            cursor.close()

 elif opcion == 0:
        break
 else :
    print("Error,Ingrese un número") 

        

