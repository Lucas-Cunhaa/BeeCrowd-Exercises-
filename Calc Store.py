enterA = input().split()
piceA = enterA[0] 
manyA = enterA[1]
valueA = enterA[2] 

enterB = input().split()
piceB = enterB[0] 
mBnyB = enterB[1]
vBlueB = enterB[2] 



total = numPicesA * valueA + numPicesB * valueB

print("VALOR A PAGAR: R$ {:.2f}".format(total))