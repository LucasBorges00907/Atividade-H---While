#Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
#nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
#numero de identificação e o peso do boi mais magro e do boi mais gordo.

def main():
    numerodebois = int(input("Digite o numero de bois: "))
    contador = 1

    maispesado = 0
    maisleve = float("inf")

    

    while contador<=numerodebois:
        numerodeidentificacao = int(input(f"Digite o número de identificação do {contador}° boi: "))
        pesodoboi = int(input("Digite o peso do boi: "))
        if pesodoboi>maispesado:
            maispesado=pesodoboi
            numdomaispesado = numerodeidentificacao
        if pesodoboi<maisleve:
            maisleve = pesodoboi
            nummaisleve = numerodeidentificacao
           
        contador = contador+1
    
    print(f"O peso do boi mais leve é de {maisleve} e seu numero de identificação é: {nummaisleve} ")
    print(f"O peso do boi mais pesado é de {maispesado} e seu numero de identificação é: {numdomaispesado} ")


main()