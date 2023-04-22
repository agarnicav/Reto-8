import math

x = float(input("Ingrese un valor para x: "))
n = int(input("Ingrese un valor para n: "))


aproximado = 0.0

for i in range(n):

    aproximado += ((x**i) / (math.factorial(i)))

actual = math.exp(x)
diff = actual - aproximado


print("Aproximación: " + str(aproximado) + ", Valor real: " + str(actual) + ", Diferencia: " + str(diff))