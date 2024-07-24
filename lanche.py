
pedido = input()  

codigo, n = pedido.split()
n = int(n)

tabela_precos = {
    "1": 4,
    "2": 4.5,
    "3": 5,
    "4": 2,
    "5": 1.5
}

if codigo in tabela_precos:
    total = tabela_precos[codigo] * n
    print(f"Total: R$ {total:.2f}")

