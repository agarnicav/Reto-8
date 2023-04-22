

n = int(input("Ingrese un número: "))

print("Los números pares en forma descendente desde 2 hasta", n, "son:")
for i in range(n, 1, -1):
    if i % 2 == 0:
        print(i)