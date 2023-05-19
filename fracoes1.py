#Leia N, calcule e escreva o valor de S.
def main():
     n = int(input("Digite N: "))
     soma = 0
     denominador = 0

     while denominador<n:
          denominador = denominador+1
          termoseguinte = 1/denominador
          soma = soma+termoseguinte
          
     print(f"Soma: {soma}")



main()