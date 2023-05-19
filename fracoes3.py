def main():
    n = int(input('Digite um número: '))
    soma = 0
    i = 1

    while i <=n:
        if i % 2 == 0:
            termo = - (n - i + 1)/i
        else:
            termo = i/(n - i + 1)
        i= i+1
        
        soma = soma + termo
                
    
    print(f"A soma dos termos é igual a {soma}")


main()