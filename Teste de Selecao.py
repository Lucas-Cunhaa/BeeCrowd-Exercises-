a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
somaAB = a + b
somaCD = c + d
par = a % 2

if b > c and d > a and somaCD > somaAB and par == 0 and c > 0 and d > 0:
    print("Valores aceitos")
else:
     print("Valores nao aceitos")

