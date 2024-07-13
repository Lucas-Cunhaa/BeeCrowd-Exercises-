n = int(float(input()) * 100)

valores = [10000,5000,2000,1000,500,200,100,50,25,10,5,1]
dinheiro = []
moedas = []
i = 0

print("NOTAS:")
for v in valores:
    i += 1 
    dinheiro.append(n // v)
    n %= v

    if i < 7:  
        print(f"{dinheiro[i - 1]:.0f} nota(s) de R$ {v / 100:.2f}")
    if i == 7:
        print("MOEDAS:")
    if i >= 7:
        print(f"{dinheiro[i - 1]:.0f} moeda(s) de R$ {v / 100:.2f}")

