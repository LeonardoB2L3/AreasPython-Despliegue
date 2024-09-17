import math

r = int(input("Dame el radio del círculo: "))
AreaCirculo = math.pi * r ** 2

l = int(input("Dame la longitud de un lado del cuadrado: "))
AreaCuadrado = l * l

B = int(input("Dame la base dek triangulo: "))
H = int(input("Dame la altura del triangulo: "))
areaTriangulo = ((B*H)/(2))

print(f"El área del círculo es: {AreaCirculo}")
print(f"El área del cuadrado es: {AreaCuadrado}")
print(f"El área del triangulo Equilatero es: {areaTriangulo}")