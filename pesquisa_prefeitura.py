#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
#número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
#escreva:
#a) média de salário da população;
#b) média de número de filhos;
#c) percentual de pessoas com salário de até R$ 1.000,00.

def main():
    numeroHabitantes = int(input("Digite o número de habitantes: "))
    
    contador = 1
    contadormenorque1000 = 0

    salariosomado = 0
    filhossomados = 0

    while numeroHabitantes>=contador:
        print(f"Pessoa {contador}:")
        salario = float(input("Salário R$: "))
        filhos = float(input('Número de filhos: '))
        

        salariosomado = salariosomado+salario
        filhossomados = filhossomados+filhos


        if salario<=1000:
            contadormenorque1000 = contadormenorque1000+1

        contador = contador+1

    media_salario = calcular_media_salario(salariosomado,numeroHabitantes)
    media_filhos = calcular_media_filhos(filhossomados,numeroHabitantes)
    percentual_abaixo_de_1000 = calcular_percentual_abaixo_de_1000(contadormenorque1000,numeroHabitantes)

    print(f"A média dos salários da população é de: R$ {media_salario}")
    print(f"A média de filhos da populção é de {media_filhos}")
    print(f"E o percentual de pessoas com salário abaixo de R$1000,00 é de {percentual_abaixo_de_1000:.2f}% ")







def calcular_media_salario(salariosomado,numeroHabitantes):
    media_salario = salariosomado/numeroHabitantes
    return media_salario

def calcular_media_filhos(filhossomados,numeroHabitantes):
    media_filhos = filhossomados//numeroHabitantes
    return media_filhos
 
def calcular_percentual_abaixo_de_1000(contadormenorque1000,numeroHabitantes):
    percentual = (contadormenorque1000/numeroHabitantes)*100
    return percentual









    
    








main()