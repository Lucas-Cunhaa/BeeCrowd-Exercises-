valores = list(map(int, input().split()))
old = valores.copy()
for i in range(len(valores) ):
   for j in range(len(valores) - 1):
      const = valores[i] 
      if valores[i] < valores[j]:
         valores[i] = valores[j]
         valores[j] = const
for i in range(len(valores) ):
    print(valores[i])
    if i == 2:
        print("")
        print(old[i - 2])
        print(old[i - 1])
        print(old[i])
 
    
 


