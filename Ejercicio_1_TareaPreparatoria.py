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
    Ejercicio 1
    
    1) Introducir numeros
    0) Apagar consola
   
    """)
 try:
        opcion = int(input("Elige una opción: ") ) 

        if opcion == 1:
            try:
                n1 = float(input("Introduce tu primer número: ") )
                n2 = float(input("Introduce tu segundo número: ") )
                n3 = float(input("Introduce tu tercer número: ") )
            

                file = open ("Ejercicio_1_TareaPreparatoria.txt", "a")
                file.write ('numero 1= %s'% n1 + '\n')
                file.write ('numero 2= %s'% n2 + '\n')
                file.write ('numero 3= %s'% n3 + '\n')

            

                if n1 > n2 and n1 > n3 and n2 != n3:
                    suma= n1+n2+n3
                    print(" ")
                    print("RESULTADO:",suma)
                    file.write ('la suma es= %s'% suma + '\n')

                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio_1(numero_1,numero_2,numero_3, resultado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,suma))
                    conexion.commit()
                    cursor.close()
                
                    
                elif n2 > n1 and n2 > n3 and n1 != n3:
                    multiplicacion= n1*n2*n3
                    print(" ")
                    print("RESULTADO:",multiplicacion)
                    file.write ('la multiplicacion es= %s'% multiplicacion + '\n')
                    
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio_1(numero_1,numero_2,numero_3, resultado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,multiplicacion))
                    conexion.commit()
                    cursor.close()

                elif n3 > n1 and n3 > n2 and n1 != n2:
                    print(" ")
                    print("RESULTADO:",n1,"",n2,"",n3)
                    n4 = [n1,n2,n3]
                    file.write ('resultado= %s'% n4 + '\n')
                    
                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio_1(numero_1,numero_2,numero_3, resultado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,n4))
                    conexion.commit()
                    cursor.close()
                
                elif n1 == n2 and n1 != n3 and n2 != n3:
                    print(" ")
                    print("RESULTADO:",n3)
                    file.write ('el numero que no es igual es = %s'% n3 + '\n')

                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio_1(numero_1,numero_2,numero_3, resultado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,n3))
                    conexion.commit()
                    cursor.close()
                    
                elif n1 == n3 and n1 != n2 and n2 != n3:
                    print(" ")
                    print("RESULTADO:",n2)    
                    file.write ('el numero que no es igual es = %s'% n2 + '\n')

                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio_1(numero_1,numero_2,numero_3, resultado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,n2))
                    conexion.commit()
                    cursor.close()
                    
                elif n2 == n3 and n2 != n1 and n3 != n1:
                    print(" ")
                    print("RESULTADO:",n1)  
                    file.write ('el numero que no es igual es = %s'% n1 + '\n')

                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio_1(numero_1,numero_2,numero_3, resultado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,n1))
                    conexion.commit()
                    cursor.close()
                    
                elif n1 == n2 and n1 == n3 and n2 == n3:
                    print(" ")
                    print("RESULTADO:","Todos son iguales")  
                    file.write ('resultado= %s'% "Todos son iguales" + '\n')

                    cursor = conexion.cursor()
                    cursor.execute("INSERT INTO ejercicio_1(numero_1,numero_2,numero_3, resultado) VALUES(%s,%s,%s,%s);",(n1,n2,n3,"Todos son iguales"))
                    conexion.commit()
                    cursor.close()

            except :  
                print("Ingrese solo numeros") 
                
        elif opcion == 0:
            break
 except :
    print("Ingrese solo numeros") 

        
 

                   
                





    




