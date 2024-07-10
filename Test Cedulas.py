valor = int(input("Digite o valor: "))
constValor = valor
notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []

for nota in notas:
    quantidades.append(valor // nota)
    valor %= nota

print(constValor)
for i in range(len(notas)):
    print(f"{quantidades[i]} nota(s) de R$ {notas[i]},00")