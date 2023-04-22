import math

x = float(input("Ingrese un valor para x: (x debe estar en el rango [-1, 1]) "))
n = int(input("Ingrese un valor para n: "))

if -1 <= x <= 1:
    approx = 0
    for i in range(n):
         term = ((-1)**i * x**(2*i+1)) / (2*i+1)
         approx += term
    actual = math.atan(x)
    diff = abs(actual - approx)
    while diff > 0.001 * abs(actual):
        n += 2
        approx = 0
        for i in range(n):
             term = ((-1)**i * x**(2*i+1)) / (2*i+1)
             approx += term
        diff = abs(actual - approx)
    
    print("Aproximación: " + str(approx) + ", Valor real: " + str(actual) + ", Diferencia: " + str(diff))
else:
    print("El valor ingresado para x no está en el rango [-1, 1]. Por favor, inténtelo de nuevo.")
