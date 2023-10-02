# CLEAR THE TERMINAL - LIMPAR TERMINAL
import os
import time #time sleep

def limpar_terminal():
    time.sleep(4)
    if os.name == 'posix':
        os.system('clear')  # Comando clear para sistemas Unix (MacOS e Linux)
    elif os.name == 'nt':
        os.system('cls')    # Comando cls para Windows



#CREATE USER - CRIAR USUARIO
#USUARIO = JOGADOR
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 3  # Vida inicial 3
        self.moeda = 1 # Moeda inicial 1

def cadastrar_usuario(nome):
    jogador = Jogador(nome)
    return jogador


#LOJA - SHOPPING

def mostrar_loja():
  from functions import cadastrar_usuario
  while True:
    print("=" * 100)
    print("")
    print("Bem-vindo à loja, aqui você pode usar suas moedas para comprar itens que podem ajudar durante o jogo.")
    print("")
    print("1. +1 Vida [2 Moedas]")
    print("2. +1 Dica [3 Moedas]")
    print("3. +1 Pulo [4 Moedas]")
    print("4. [Sair da Loja]")
    print("")
    print("=" * 100)
    print("")
    
    while True:
        try:
            escolha = int(input("Digite de 1 a 4 para escolher uma opção: "))
            if escolha not in [1, 2, 3, 4]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print(f"Erro: apenas de 1 a 4.")
            
            #ESSE IF TA COM ERRO
    if escolha == 1:
      if jogador.moeda < 2:
        print("Você não tem moedas suficientes!")
      else:
        jogador.vida += 1
        jogador.moeda -= 2  # Deduz as moedas após a compra
        print(f"Você comprou +1 Vida! Agora você tem {jogador.vida} vidas e {jogador.moeda} moedas.")


  






