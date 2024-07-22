ddd = input()
modal = True

cidades = {
    "11": "Sao Paulo", 
    "61": "Brasilia",
    "71": "Salvador",
    "21": "Rio de Janeiro",
    "32": "Juiz de Fora",
    "19": "Campinas",
    "27": "Vitoria",
    "31": "Belo Horizonte"
}

for num, cidade in cidades.items():
    if num == ddd:
        print(cidade)
        modal = False
        break

if modal:
    print("DDD nao cadastrado")