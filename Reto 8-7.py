
# Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

for u in range(1,10):
    print( "esta es la tabla del " +str(u))
    for j in range(1, 11):
       Tabla= u*j
       print(str(u) +"x" +str(j)+ "= " + str(Tabla))
    
