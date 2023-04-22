# Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for.

x = float(input("Ingrese un número: "))
n = int(input("ingrese otro número: "))

for u in range(1,n+1) :
   h = x ** u
   print(h)