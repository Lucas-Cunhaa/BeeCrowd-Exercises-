a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

areaTriangulo = a * c /2 
areaCirculo =  c ** 2 * 3.14159 
areaTrapezio = (a + b) * c / 2
areaQuadrado = b ** 2 
areaRetangulo =  a * b 

print(f"TRIANGULO: {areaTriangulo:.3f}")
print(f"CIRCULO: {areaCirculo:.3f}")
print(f"TRAPEZIO: {areaTrapezio:.3f}")
print(f"QUADRADO: {areaQuadrado:.3f}")
print(f"RETANGULO: {areaRetangulo:.3f}")

