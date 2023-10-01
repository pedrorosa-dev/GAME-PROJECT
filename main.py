import time 
from functions import limpar_terminal
from functions import cadastrar_usuario

#INTRODUCTION - INTRODUÇÃO
time.sleep(0.2)
print('-'*100)
print("Bem vindos ao nome do game")
time.sleep(2.5)
print("O jogador terá inicialmente três tentativas para acertar corretamente as perguntas ate chegar no one piece")
print('-'*100)
time.sleep(4)
limpar_terminal()

#CREATE A PLAYER  - CRIANDO O JOGADOR
#USUARIO = JOGADOR 
nome_usuario = input("Digite o nome do jogador: ")
time.sleep(1.2)
usuario = cadastrar_usuario(nome_usuario)
print(f"Ola, {usuario.nome}! vamos começar nossa jornada? espero que esteja pronto por que o caminho não será nada facil! ")
