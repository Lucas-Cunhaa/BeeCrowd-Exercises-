a, b = input().split()
a, b = int(a), int(b)

restoAB = a % b 
restoBA = b % a
if  restoAB and restoBA:
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")