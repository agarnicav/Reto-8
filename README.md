# Primer punto 

Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

          # Se utiliza la función range() para generar los números del 1 al 100 y se itera sobre ellos con un bucle for
          for n in range(1, 101):
          # Se imprime el número actual junto con su cuadrado, utilizando la función str() para convertir los números en cadenas de texto
               print("El cuadrado del numero " + str(n) + " es " + str(n**2))



# Segundo punto 

Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


      # Se utiliza la función range() para generar los números impares desde 1 hasta 999 y se itera sobre ellos con un bucle for
        print("los numeros impares desde 1 hasta 999 son")
        for i in range(1, 1000, 2):
             print(i)  # se imprime la lista de numeros desde 1 a 999 que son impares

      # Se utiliza la función range() para generar los números pares desde 2 hasta 1000 y se itera sobre ellos con un bucle for
         print("los numeros pares desde 2 hasta 1000 son")
         for u in range(2, 1001, 2):
         print(u)   # se imprime la lista de numeros desde 2 a 1000 que son pares



# Tercer punto 

Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

       # Se solicita ingresar un número entero y se almacena en la variable n.
       n = int(input("Ingrese un número: "))

       # Se utiliza un ciclo for para iterar desde el número n hasta el número 2 en orden descendente.
       # Se verifica si cada número en el ciclo es divisible por 2, si lo es, se imprime el número.
       print("Los números pares en forma descendente desde 2 hasta", n, "son:")
       for i in range(n, 1, -1):
             if i % 2 == 0:
               print(i)
               
               
               
# Cuarto punto 

Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

        # Se solicita ingresar un número entero y se almacena en la variable n.
        n = int(input("Ingrese un número: "))

        # Se utiliza un ciclo for para iterar desde el número 1 hasta el número n ingresado por el usuario.
        # Para cada número en el ciclo, se calcula su factorial utilizando otro ciclo for interno.
        # El factorial se calcula multiplicando el número actual por todos los números enteros positivos menores o iguales a él.
        # Finalmente, se imprime el número y su factorial en la salida.
        for i in range(1, n+1):
            factorial = 1
            for j in range(1, i+1):
                factorial *= j
            print(str(i) + " y su factorial es " + str(factorial))

# Quinto punto

Calcular el valor de 2 elevado a la potencia n usando ciclos for.

       # Se solicita ingresar un número entero y se almacena en la variable n.
       n = int(input("Ingrese un número: "))

       # Se utiliza un ciclo for para iterar desde 1 hasta el número ingresado por el usuario.
       # En cada iteración se calcula el valor de 2 elevado a la potencia actual (u).
       # Se imprime el resultado de cada potencia en la salida.
       for u in range(1,n+1): 
           h= 2**u
          print(h)
          
          

# Sexto punto 

Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

       # Se solicita ingresar un número real x y un número natural n y se almacenan en las variables correspondientes.
       x = float(input("Ingrese un número: "))
       n = int(input("Ingrese otro número: "))

       # Se utiliza un ciclo for para iterar desde 1 hasta el número n ingresado por el usuario.
       # En cada iteración se calcula el valor de x elevado a la potencia actual (u).
       # Se imprime el resultado de cada potencia en la salida.
       for u in range(1, n+1):
           h = x ** u
           print(h)


# Septimo punto

Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

        # Se utiliza un ciclo for para iterar desde 1 hasta 9 para mostrar las tablas de multiplicar del 1 al 9.
        for u in range(1,10):
        # Se imprime el número de la tabla actual.
            print("Esta es la tabla del " +str(u))
        # Se utiliza otro ciclo for para iterar desde 1 hasta 10 para mostrar los resultados de la tabla actual.
            for j in range(1, 11):
                Tabla= u*j
                print(str(u) +"x" +str(j)+ "= " + str(Tabla))
                
                
# Octavo punto

Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

![8](https://user-images.githubusercontent.com/124607325/233765041-36ef1ecf-4fe2-4711-9e76-54febb690ead.png)

       import math
       # Se pide al usuario que ingrese un valor para x y n
       x = float(input("Ingrese un valor para x: "))
       n = int(input("Ingrese un valor para n: "))

       # Inicializa la variable de la aproximación en 0
       aproximado = 0.0

       # Ciclo for que itera n veces para calcular la aproximación
       for i in range(n):
       # Calcula el término correspondiente de la serie de Maclaurin y lo agrega a la aproximación
           aproximado += ((x**i) / (math.factorial(i)))

# Calcula el valor real de la función exponencial
actual = math.exp(x)

# Calcula la diferencia entre el valor real y la aproximación
diff = actual - aproximado

# Imprime los resultados
print("Aproximación: " + str(aproximado) + ", Valor real: " + str(actual) + ", Diferencia: " + str(diff))




