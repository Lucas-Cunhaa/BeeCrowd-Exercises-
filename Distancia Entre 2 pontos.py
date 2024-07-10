xA, yA = input().split()
xB, yB = input().split()
xA, yA, xB, yB = float(xA), float(yA), float(xB), float(yB)

distancia = (( xB - xA ) **2  + ( yB - yA ) ** 2) ** (1/2)
           

print(f"{distancia:.4f}")