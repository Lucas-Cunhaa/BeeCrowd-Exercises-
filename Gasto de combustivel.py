autonomia = 12 
tempo = int(input())
velocidade = int(input())

distancia = tempo * velocidade 
litro = distancia / autonomia

print(f"{litro:.3f}")