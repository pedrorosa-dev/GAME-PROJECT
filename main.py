import time 
from functions import limpar_terminal
from functions import cadastrar_usuario

# INTRODUCTION - INTRODUÇÃO
time.sleep(0.2)
print('-' * 200)
print("Bem vindos ao nome do game")
time.sleep(2.5)
print("O jogador terá inicialmente três tentativas para acertar corretamente as perguntas até chegar no one piece")
print('-' * 200)
time.sleep(6)
limpar_terminal()

# CREATE A PLAYER - CRIANDO O JOGADOR
# USUARIO = JOGADOR 
while True:
    try:
        nome_jogador = input("Digite o nome do jogador: ")
        if not nome_jogador:
            raise ValueError("O nome do jogador não pode estar vazio.")
        jogador = cadastrar_usuario(nome_jogador)
        break  # Sai do loop se um nome válido for digitado
    except ValueError as error:
        print(f"Erro: {error}. Por favor, digite um nome válido.")

time.sleep(2.2)
print(f"Olá, {jogador.nome}! Vamos começar nossa jornada? Espero que esteja pronto, porque o caminho não será nada fácil!")
time.sleep(2.2)
print("Carregando...")
time.sleep(3.5)
limpar_terminal()

# INITIAL GAME - INÍCIO DO GAME

#PRIMEIRA PERGUNTA
print('-' * 200)
print(f"Jogador: {jogador.nome}")
print(f"Vida: {jogador.vida}")
