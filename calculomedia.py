#----------------------------------------------
# Teste de cálculo e tomada de decisão
#
# Conceito A = nota >= 9 and < 10
# Conceito B = nota >= 8 and 8,99999
# Conceito C = nota >= 7 and 7,99999
# Conceito D = nota >= 6 and 6,99999
# Conceito R = nota < 5
#
#----------------------------------------------
from termcolor import colored


def main():
    
    nota1 = float(input('Digite a primeira nota 1: '))
    nota2 = float(input('Digite a primeira nota 2: '))
    nota3 = float(input('Digite a primeira nota 3: '))
    nota4 = float(input('Digite a primeira nota 4: '))

    print(colored('Seus Resultados', 'blue'))
#    print('Seus Resultados')
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f'Sua média é {media}.')

    if media >= 9 and media < 10:
        print('Conceito A')
    elif media >= 8 and media < 9:
        print('Conceito B')
    elif media >= 7 and media < 8:
        print('Conceito C')
    elif media >= 6 and media < 7:
        print('Conceito D')
    elif media < 6:
        print('Conceito R')
main()