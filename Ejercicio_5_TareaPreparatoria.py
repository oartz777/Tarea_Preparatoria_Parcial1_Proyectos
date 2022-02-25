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
    n1= input_numero("Ingrese el primer numero: ")
    n2= input_numero("Ingrese el segundo numero: ")
    if n1 < n2:
        serie=list(range(n2, n1-1, -1))
        print(serie)

        file = open ("Ejercicio_5_TareaPreparatoria.txt", "a")
        file.write ('Numero de origen= %s'% n2  + '\n')
        file.write ('Numero final= %s'% n1  + '\n')
        file.write ('Los numeros de mayor a menor: %s'% serie  + '\n')
        file.write ('-----------------------------------------''\n')

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ejercicio_5(numero_origen,numero_final,rango) VALUES(%s,%s,%s);",(n2,n1,serie))
        conexion.commit()
        cursor.close()

    elif n1 > n2:
        serie=list(range(n1, n2-1, -1))
        print(serie)

        file = open ("Ejercicio_5_TareaPreparatoria.txt", "a")
        file.write ('Numero de origen= %s'% n1  + '\n')
        file.write ('Numero final= %s'% n2  + '\n')
        file.write ('Los numeros de mayor a menor: %s'% serie  + '\n')
        file.write ('-----------------------------------------''\n')

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ejercicio_5(numero_origen,numero_final,rango) VALUES(%s,%s,%s);",(n1,n2,serie))
        conexion.commit()
        cursor.close()

        
    else :
        print("sus numeros son iguales")

        file = open ("Ejercicio_5_TareaPreparatoria.txt", "a")
        file.write ('Numero de origen= %s'% n2  + '\n')
        file.write ('Numero final= %s'% n1  + '\n')
        file.write ('Los numeros son iguales' + '\n')
        file.write ('-----------------------------------------''\n')

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO ejercicio_5(numero_1,numero_2,rango) VALUES(%s,%s,%s);",(n1,n2,'Son iguales'))
        conexion.commit()
        cursor.close()

    