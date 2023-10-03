import time 
import sys
from functions import limpar_terminal
from functions import cadastrar_usuario
from functions import mostrar_loja
from functions import tempo_resposta
from functions import cena

#MENU LOGIN
# Dicionário para armazenar nomes de usuário e senhas
usuarios = {}
logado = False  # Variável para controlar se o usuário está logado

while True:
    print("="*100)
    print("Menu:")
    print("")
    print("1 - Fazer login")
    print("2 - Registrar")
    print("3 - Entrar no jogo")
    print("4 - Sair do jogo")
    print("="*100)
    

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Fazer login
        print("")
        nome_usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        if nome_usuario in usuarios and usuarios[nome_usuario] == senha:
            print("")
            print("Login bem-sucedido!")
            logado = True
            cena()
        else:
            print("")
            print("Nome de usuário ou senha incorretos.")
            logado = False
            cena()

    elif opcao == "2":
        # Registrar
        print("")
        nome_usuario = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")

        if nome_usuario in usuarios:
            print("")
            print("Nome de usuário já existe. Escolha outro.")
            cena()
        else:
            usuarios[nome_usuario] = senha
            print("")
            print("Registro bem-sucedido!")
            cena()

    elif opcao == "3":
        # Entrar no jogo
        if logado:
            cena()
            break

        else:
            print("")
            print("Você precisa fazer login para entrar no jogo.")
            cena()


    elif opcao == "4":
        # Sair do programa
        print("")
        print("Finalizando o jogo...")
        time.sleep(0.8)
        cena()
        sys.exit() #vai finalizar o programa

    else:
        print("")
        print("Erro: Opção inválida.")
        cena()


# INTRODUCTION - INTRODUÇÃO
print('=' * 100)
print("Bem vindos ao nome do game")
print("")
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
        print("")
        time.sleep(0.1)
        if not nome_jogador.strip():#SE DIGITAR ESPACO E DER ENTER ELE FUNCIONA! TEM QUE AJEITAR
            raise ValueError
        jogador = cadastrar_usuario(nome_jogador)
        break  # Sai do loop se um nome válido for digitado
    except ValueError:
        print("")
        print(f"Erro: Por favor, digite um nome válido.")
        print("")
        
print("=" *100)
print("")

print(f"Olá, {jogador.nome}! Vamos começar nossa jornada? Espero que esteja pronto, porque o caminho não será nada fácil!")
tempo_resposta()
print("Carregando...")
limpar_terminal()

#LOJA
mostrar_loja(jogador)