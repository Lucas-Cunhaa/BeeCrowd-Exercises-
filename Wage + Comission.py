name = input() 
fix_wage = float(input())
comission = float(input()) 

wage = comission * (15/100) + fix_wage 

print("TOTAL = R$ {:.2f}".format(wage))