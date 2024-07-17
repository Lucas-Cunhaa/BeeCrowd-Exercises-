n1, n2 ,n3 ,n4 = map(float, input().split())

media = ( 2 * n1 + 3 * n2 + 4 * n3 + 1 * n4 ) / 10
print(f"Media: {media:.1f}")
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    media = (nota_exame + media) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")

