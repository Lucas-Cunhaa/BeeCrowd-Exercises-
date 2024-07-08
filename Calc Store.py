enterA = input().split()
piceA = int(enterA[0]) 
manyA = int(enterA[1])
valueA = float(enterA[2]) 

enterB = input().split()
piceB = int(enterB[0]) 
manyB = int(enterB[1])
valueB = float(enterB[2]) 



total = manyA * valueA + manyB * valueB

print("VALOR A PAGAR: R$ {:.2f}".format(total))