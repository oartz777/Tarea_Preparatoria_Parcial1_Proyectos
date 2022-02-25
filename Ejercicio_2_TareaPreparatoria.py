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
 numero = input_numero("Introduce un numero: ")

 def divisores(numero):

    resultado = [i for i in range(1, numero +1) if numero %i == 0]
    return resultado
 numero2 = divisores(numero)
 print(numero2)

 file = open ("Ejercicio_2_TareaPreparatoria.txt", "a")
 file.write ('numero= %s'% numero + '\n')
 file.write ('divisores= %s'% numero2  + '\n')

 cursor = conexion.cursor()
 cursor.execute("INSERT INTO ejercicio_2(numero,divisores) VALUES(%s,%s);",(numero,numero2))
 conexion.commit()
 cursor.close()

    



