import math

r = int(input("Dame el radio del círculo: "))
AreaCirculo = math.pi * r ** 2

l = int(input("Dame la longitud de un lado del cuadrado: "))
AreaCuadrado = l * l
        
print(f"El área del círculo es: {AreaCirculo}")
print(f"El área del cuadrado es: {AreaCuadrado}")
