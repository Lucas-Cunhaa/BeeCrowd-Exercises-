num = float(input())
n = 0
taxa = 0
resto = 0

if num > 4500 :
    n = num // 4500
    num %= 4500

    while n > 1:
        n -=1 
        num += 4500
    
    taxa += (num * 28/100 ) 
    taxa += (1500 * 18/100)
    taxa += (1000 * 8/100 )
    print(f"R$ {taxa:.2f}")

elif 3000.01 <= num <= 4500 :
    n = num // 3000.01
    num %= 3000.01

    while n > 1:
        n -=1 
        num += 3000.01
    taxa += (num * 18/100 ) 
    taxa += (1000 * 8/100 )
    print(f"R$ {taxa:.2f}")

elif 2000.01 <= num < 3000 :
    n = num // 2000.01
    num %= 2000.01

    while n > 1:
        n -=1 
        num += 2000.01
    taxa += (num * 8/100 )
    print(f"R$ {taxa:.2f}")

else:
    print("Isento")

