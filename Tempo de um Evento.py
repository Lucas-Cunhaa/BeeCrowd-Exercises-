d1 = int(input().split()[1])
h1, m1, s1 = map(int, input().split(":"))
t1 = s1 + m1*60 + h1*60*60 + d1 * 24 * 60 *60

d2 = int(input().split()[1])
h2, m2, s2 = map(int, input().split(":"))
t2 = s2 + m2*60 + h2*60*60 + d2 * 24 * 60 *60

dif = t2 - t1

dias = dif // (24 * 60 *60) 
dif %= (24 * 60 *60) 

horas = dif //  (60 *60)
dif %= 60*60

minutos = dif // 60 
dif %= 60 

segundos = dif

print(dias, "dia (s)")
print(horas, "hora(s)")
print(minutos, "minuto(s)")
print(segundos, "segundo(s)")