#Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
#  pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random#numero aleatorio
from time import sleep #paralisar o tempo por alguns segundos
computador= random.randint(0,5)
print('\033[31m-=-\33[m'*18  )
print('\033[34m vou pensar em um numero de 0 a 5, tente adivinhar! ')
print('\033[31m-=-\033[m'*18)
num = int(input('\033[36m Em qual numero eu pensei? '))#jogador pensa no numero
print('\033[0;33m PROCESSING...\033[m')
sleep(3)
if num == computador:
    print('\033[32m O numero que voce escolheu foi \033[31m {}'.format(num))
    print('\033[32mParabens você acertou \033[31m *---* \033[32m o numero que eu escolhi foi \033[31m {}'.format(computador))
else:
    print('\033[32m HAHA! voce errou !')
    print('Eu ganhei! o numero que eu pensei foi \033[31m{}\033[32m, e voce escolheu \033[31m{}'.format(computador, num))
