valor = int(input())
constValor = valor
nota100 =  0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0


while valor > 0:
    if valor >= 100:
        nota100 = valor // 100
        valor = valor % 100 
    elif valor >= 50 :
        nota50 = valor // 50
        valor = valor % 50
    elif valor >= 20:
        nota20 = valor // 20
        valor = valor % 20
    elif valor >= 10:
        nota10 = valor // 10
        valor = valor % 10
    elif valor >= 5:
        nota5 = valor // 5
        valor = valor % 5
    elif valor >= 2:
        nota2 = valor // 2
        valor = valor % 2
    else : 
        nota1 = valor // 1
        valor = valor % 1
print(constValor)       
print(f"{nota100} nota(s) de R$ 100,00")
print(f"{nota50} nota(s) de R$ 50,00")
print(f"{nota20} nota(s) de R$ 20,00")
print(f"{nota10} nota(s) de R$ 10,00")
print(f"{nota5} nota(s) de R$ 5,00")
print(f"{nota2} nota(s) de R$ 2,00")
print(f"{nota1} nota(s) de R$ 1,00")