
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
import os
from termcolor import colored

def main():
    os.system('clear') or None
    
    print(colored('Digite os valores das notas, use ponto para separar decimais', color='green'))
    
    nota1 = float(input('Digite a primeira nota 1: '))
    nota2 = float(input('Digite a primeira nota 2: '))
    nota3 = float(input('Digite a primeira nota 3: '))
    nota4 = float(input('Digite a primeira nota 4: '))

    print(colored('Seus Resultados', color='blue'))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(colored(f'Sua média é {media}.', color='green'))

    if media >= 9 and media < 10:
        print(colored('Conceito A', color='red', attrs=['bold']))
    elif media >= 8 and media < 9:
        print(colored('Conceito B', color='magenta', attrs=['dark']))
    elif media >= 7 and media < 8:
        print(colored('Conceito C', color='yellow', attrs=['blink']))
    elif media >= 6 and media < 7:
        print(colored('Conceito D', color='cyan', attrs=['reverse']))
    elif media < 6:
        print(colored('Conceito R', color='green', attrs=['bold', 'blink', 'reverse']))
main()