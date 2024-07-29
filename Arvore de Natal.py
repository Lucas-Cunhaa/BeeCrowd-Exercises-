altura = int(input())
for i in range(1, altura + 1):
    o = "o" * ( 1 + (i - 1) * 2)
    espaco = ' ' * (altura - i)
    print(f"{espaco}{o}")