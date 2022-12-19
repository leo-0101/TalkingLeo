from time import sleep
import os
import random


def intro():
    print('~'*55)
    print('OLÁ! ESSE É O TALKING LEO!')
    sleep(0.5)
    print('FAÇA UMA PERGUNTA E RECEBA UMA RESPOSTA SINCERA!')
    print('~'*55)


lista_respostas = ['SIM', 'CLARO QUE SIM', 'NÃO', 'ÓBVIO QUE NÃO', 'TALVEZ', 'QUEM SABE UM DIA...']

intro()
input('TECLE [ENTER] PARA CONTINUAR')
print()
os.system('cls')

while True:
    input('FAÇA SUA PERGUNTA AO LEO: ')
    print('LEO ESTÁ PERGUNTANDO AOS ASTROS...')
    sleep(1.0)
    print('SUA RESPOSTA É: ', random.choice(lista_respostas))
    input()
    os.system('cls')
