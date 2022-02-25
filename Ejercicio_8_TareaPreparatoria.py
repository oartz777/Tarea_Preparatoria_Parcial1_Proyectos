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

while True:
 print("""
    Ejercicio 8
    
    1) Mostrar los numeros impares del 1 al 100
    2) Ver historial
    0) Apagar consola
   
    """)
 try:
            opcion = int(input("Elige una opción: ") ) 

            if opcion == 1:
                
                serie=list(range(1, 100, 2 ))
                print(serie)
                impares = len((serie))
                print("los numeros impares son:", impares)

                file = open ("Ejercicio_8_TareaPreparatoria.txt", "a")
                file.write ('Los numeros impares del 1 al 100 son: %s'% serie + '\n')
                file.write ('Los numeros impares son en total: %s'% impares + '\n')
                

                cursor = conexion.cursor()
                cursor.execute("INSERT INTO ejercicio_8(listado,numero_impares) VALUES(%s,%s);",(serie,impares))
                conexion.commit()
                cursor.close()
            

            if opcion == 2:

                cursor = conexion.cursor()
                SQL = 'SELECT*FROM ejercicio_8;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
                cursor.close()
                

            if opcion == 0:
                break

 except :
  print("Ingrese solo numeros") 


    
    