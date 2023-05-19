#Leia N, calcule e escreva o valor de S.

def main():
     n = int(input("Digite N: "))
     soma = 0
     contador = 1

     while contador<=n:
           termo = contador/(n - contador + 1)
           soma = soma + termo
           contador = contador + 1
          
     print(f"Soma: {soma}")



main()