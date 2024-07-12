dias = int(input())

anos = dias // 365 
dias %= 365 

meses = dias // 12 
dias = dias % 12

print(anos, meses, dias)