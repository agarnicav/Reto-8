x = float(input("Ingrese un valor para x: "))
n = int(input("Ingrese un valor para n: "))
import math

aproximado = 0.0
for i in range(n):
    aproximado += (-1)**i * x**(2*i+1) / math.factorial(2*i+1)


actual = math.sin(x)
diff = abs(actual - aproximado)
    
print("Aproximación: " + str(aproximado) + ", Valor real: " + str(actual) + ", Diferencia: " + str(diff))