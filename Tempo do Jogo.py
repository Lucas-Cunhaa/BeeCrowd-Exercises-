h1, m1, h2, m2 = map(int, input().split())
t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

if t2 <= t1:
    t2 += 24 * 60  
    
dif = t2 - t1

h = dif // 60
m = dif % 60

print(f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")
