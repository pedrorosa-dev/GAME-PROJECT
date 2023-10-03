import time 
from functions import limpar_terminal
from functions import cadastrar_usuario
from functions import mostrar_loja
from functions import tempo_resposta

# INTRODUCTION - INTRODUÇÃO
#tempo_resposta()
print('=' * 100)
print("")
print("Bem vindos ao nome do game")
print("")
#tempo_resposta()
print("O jogador terá inicialmente três tentativas para acertar corretamente as perguntas até chegar no one piece")
print("")
print('=' * 100)
limpar_terminal()

# CREATE A PLAYER - CRIANDO O JOGADOR
# USUARIO = JOGADOR
print("="*100) 
print("")
while True:
    try:
        nome_jogador = input("Digite o nome do jogador: ")
        if not nome_jogador:
            raise ValueError
        jogador = cadastrar_usuario(nome_jogador)
        break  # Sai do loop se um nome válido for digitado
    except ValueError:
        print("")
        print(f"Erro: Por favor, digite um nome válido.")
        print("")
        
print("=" *100)
print("")

#tempo_resposta()
print(f"Olá, {jogador.nome}! Vamos começar nossa jornada? Espero que esteja pronto, porque o caminho não será nada fácil!")
#tempo_resposta()
print("Carregando...")
limpar_terminal()

# INITIAL GAME - INÍCIO DO GAME

#PRIMEIRA PERGUNTA
print('=' * 100)
print(f"Jogador: {jogador.nome}")
print(f"Vida: {jogador.vida}")
print(f"Moeda: {jogador.moeda}")

mostrar_loja(jogador)