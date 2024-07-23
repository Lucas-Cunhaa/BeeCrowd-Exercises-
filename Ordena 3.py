num1 = int(input())
num2 = int(input())
num3 = int(input())

list = [num1, num2, num3]

for i in range(len(list)):
    for j in range(len(list) - 1 - i):
        if list[j] > list[j + 1]:
             list[j], list[j + 1] = list[j + 1], list[j]
        print(list)