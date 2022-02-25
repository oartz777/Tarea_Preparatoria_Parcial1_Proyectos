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

 def obtener_vocales(frase):
    vocales='aeiouAEIOU'

    return[c for c in frase if c in vocales]

 frase= input("Ingrese una Palabra: ")
 vocal= len(obtener_vocales(frase))
 print("La palabra tiene", vocal, "vocales")

 file = open ("Ejercicio_3_TareaPreparatoria.txt", "a")
 file.write ('palabra= %s'% frase  + '\n')
 file.write ('El numero de vocales de la palabra son= %s'% vocal + '\n')
 
 cursor = conexion.cursor()
 cursor.execute("INSERT INTO ejercicio_3(palabra,numero_de_vocales) VALUES(%s,%s);",(frase,vocal))
 conexion.commit()
 cursor.close()

