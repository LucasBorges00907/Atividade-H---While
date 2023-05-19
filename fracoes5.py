

def main():
    n = int(input("Insira n: "))
    contador = 1
    soma=0
    


    while contador<=n:
        numerador = 2*contador-1
        denominador= contador
        termo = numerador/denominador
        soma = soma+termo
        contador = contador+1

    print(f"A Soma dos termos até n é de: {soma}")

main()