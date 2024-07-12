n = int(input())
horas = n // 3600
restoH = n % 3600 #RESTO EM SEGUNDOS 

if restoH < 60:
    segundos = restoH
    print(f"{horas}:{0}:{segundos}")
else:
    restoM = restoH % 60
    minutos = restoH // 60 
    segundos = restoM
    print(f"{horas}:{minutos}:{segundos}")
    



