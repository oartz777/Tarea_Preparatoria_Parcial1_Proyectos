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

frase = input("Ingrese una palabra: ")
frase = frase.lower()
vocales = ["a","e","i","o","u"]

file = open ("Ejercicio_6_TareaPreparatoria.txt", "a")
file.write ('----------------------------------' '\n')
file.write ('Vocales de la palabra: %s'% frase + '\n')


for x in vocales:
    veces=0
    for y in frase:
        if x==y:
            veces+=1
    print("La vocal", x, "aparece", veces, "veces")

    file.write ('La vocal %s' % x + 'aparece: %s'% veces + 'veces' '\n')

    cursor = conexion.cursor()
    SQL = "INSERT INTO ejercicio_6(palabra, vocales, veces) VALUES( %s,%s,%s)" 
    cursor.execute(SQL,(frase,x,veces))
    conexion.commit()
    cursor.close() 