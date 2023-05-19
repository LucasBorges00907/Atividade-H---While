#Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
#horas trabalhadas e o seu número de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
#40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
#Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
#funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
#líquido do funcionário.

def main():

    numerofuncionarios = int(input("Escreva o número de funcionários: "))

    salarioporhora = 12
    valorpordependente = 40
    descontoinss = 8.5/100
    descontoimpostoderenda = 5/100

    contador = 1

    while contador<=numerofuncionarios:
        print(f"Funcionário: {contador}")
        codigo = int(input("Escreva o seu código: "))
        horastrabalhadas = int(input("Escreva o número de horas trabalhadas: "))
        numerodedependentes = int(input("Escreve o número de dependentes: "))

        salariobruto = (horastrabalhadas*salarioporhora) + (numerodedependentes*valorpordependente)
        valordescontoinss = descontoinss*salariobruto
        valordescontoir = descontoimpostoderenda*salariobruto

        salarioliquido = salariobruto-valordescontoir-valordescontoinss

        contador = contador+1

        print(f"Desconto INSS: R${valordescontoinss:.2f}")
        print(f"Valor desconto Imposto de Renda: R${valordescontoir:.2f}")
        print(f"Salário líquido: {salarioliquido:.2f}")







        












main()
