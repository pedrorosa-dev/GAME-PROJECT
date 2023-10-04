import os
import sys#biblioteca para finalizar o codigo
import time #time sleep
# CLEAR THE TERMINAL - LIMPAR TERMINAL

def limpar_terminal():
    time.sleep(2.6)
    if os.name == 'posix':
        os.system('clear')  # Comando clear para sistemas Unix (MacOS e Linux)
    elif os.name == 'nt':
        os.system('cls')    # Comando cls para Windows

def cena():
    time.sleep(1.4)
    if os.name == 'posix':
        os.system('clear')  # Comando clear para sistemas Unix (MacOS e Linux)
    elif os.name == 'nt':
        os.system('cls')    # Comando cls para Windows

#TEMPO TIME SLEEP
def tempo_resposta():
  time.sleep(2.2)


#CREATE USER - CRIAR USUARIO
#USUARIO = JOGADOR
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 0  # Vida inicial 3
        self.moeda = 0# Moeda inicial 1
        self.pulo = 0#pulo inicial 0

def cadastrar_usuario(nome):
    jogador = Jogador(nome)
    return jogador


#LOJA - SHOPPING

def mostrar_loja(jogador: object):
  while True:
    print('=' * 100)
    print("")
    print(f"Jogador: {jogador.nome}")
    print(f"Vida: {jogador.vida}")
    print(f"Moeda(s): {jogador.moeda}")
    print(f"Pulos Disponiveis: {jogador.pulo}")
    print("")
    print("=" * 100)
    print("")
    print("Bem-vindo à loja, aqui você pode usar suas moedas para comprar itens que podem ajudar durante o jogo.")
    print("")
    print("1. + 1 Vida [2 Moedas]")
    print("")
    print("2. + 1 Pulo [4 Moedas]")
    print("")
    print("3. [Sair da Loja]")
    print("")
    print("=" * 100)
    print("")
    
    while True:
        try:
            escolha = int(input("Digite de 1 a 3 para escolher uma opção: "))
            if escolha not in [1, 2, 3, ]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 3.")
            cena()
            
        
    if escolha == 1:
      if jogador.moeda < 2:
        print("=" *100)
        print("")
        print("Você não tem moedas suficientes!")
        print("")
        time.sleep(0.1)
        cena()
      else:
        jogador.vida += 1
        jogador.moeda -= 2  # Deduz as moedas após a compra
        print("")
        print(f"Você comprou + 1 Vida! Agora você tem {jogador.vida} vidas e {jogador.moeda} moedas.")
        time.sleep(0.1)
        cena()
    
    elif escolha == 2:
      if jogador.moeda >= 4:
        print(f"{jogador.nome}, Você ganhou um pulo!!")
        jogador.pulo += 1
        jogador.moeda -=4
        cena()
      else:
        print("="*100)
        print("")
        print(f"{jogador.nome}, Você precisa mais de 4 moedas pra poder usar esse item...")
        cena()
      
  
    
    elif escolha == 3:
      print("")
      print("Voltando...")
      time.sleep(0.5)
      cena()
      break


#MENU DO TEMAS - theme
def menu_temas(jogador: object):
  jogador.vida = 3
  jogador.moeda = 1
  jogador.pulo = 0
  while True:
    print("=" * 100)
    print("")
    print(f"Jogador: {jogador.nome}")
    print("")
    print("="*100)
    print("")
    print("[TEMAS]")
    print("")
    print("<<1>> Entretenimento")
    print("<<2>> Programação")
    print("<<3>> Matemática")
    print("<<4>> Finalizar jogo")
    print("")
    print("=" * 100)
    print("")
    
    while True:
        try:
            escolha = int(input("Digite de 1 a 4 para escolher uma opção: "))
            cena()
            if escolha not in [1, 2, 3, 4]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            
            print(f"Erro: apenas de 1 a 4.")
            
    if escolha ==  1:
        cena()
        entretenimento(jogador)
        
    #elif escolha == 2:
        #cena()
        #programacao(jogador)
        
    #elif escolha ==3:
        #cena()
        #matematica(jogador)
        
    elif escolha == 4:
        # Sair do programa - Leave the program
        print("")
        print("Finalizando o jogo...")
        time.sleep(0.8)
        cena()
        sys.exit()  # Vai finalizar o programa
    else:
        print("")
        print("Erro: Opção inválida.")
        cena()
      

#TEMA - ENTRETEIDIMENTO -FUN - TEMA 1 - 1 PERGUNTA
def entretenimento(jogador: object):
  jogador.vida = 3
  jogador.moeda = 1
  jogador.pulo = 0
  while True:
    print("="*100)
    print("")
    print("[Entreterimento]")
    print("")
    print("="*100)
    print("")
    print(f"Vida: {jogador.vida}")
    print(f"Moeda: {jogador.moeda}")
    print(f"Pulos Disponiveis: {jogador.pulo}")
    print("=" * 100)
    print("")
    print("[Pergunta 1]")
    print("")
    print("Qual ator interpretou o personagem Jack Dawson no filme 'Titanic' de 1997?")
    print("")
    print("1) Leonardo DiCaprio")
    print("2) Johnny Depp")
    print("3) Brad Pitt")
    print("4) Tom Hanks")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    
    
    while True:
        try:
            escolha_entretenimento = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_entretenimento not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_entretenimento == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_entretenimento == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        break
    
    if escolha_entretenimento != 1 and escolha_entretenimento < 5:
      cena()
      jogador.vida -= 1
      if jogador.vida < 1:
        print("="*100)
        print("")
        print("Game Over! VOCÊ PERDEU O GAME :(")
        print("")
        print("="*100)
        limpar_terminal()
        
        menu_temas(jogador)
      else:
        print("")
        print("Resposta incorreta, tente mais uma vez!")
        print("")
    
    elif escolha_entretenimento == 1 and escolha_entretenimento < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
  
  while True: # TEMA 1 - PERGUNTA 2
    print("="*100)
    print("")
    print("[Entreterimento]")
    print("")
    print("="*100)
    print("")
    print(f"Vida: {jogador.vida}")
    print(f"Moeda: {jogador.moeda}")
    print(f"Pulos Disponiveis: {jogador.pulo}")
    print("=" * 100)
    print("")
    print("[Pergunta 2]")
    print("")
    print("Qual é a série de televisão mais longa da história, com mais de 30 temporadas?")
    print("")
    print("1) Friends")
    print("2) The Simpsons")
    print("3) The Big Bang Theory")
    print("4) Game of Thrones")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    

    while True:
        try:
            escolha_entretenimento = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_entretenimento not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_entretenimento == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_entretenimento == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        break
    
    if escolha_entretenimento != 2 and escolha_entretenimento < 5:
      cena()
      jogador.vida -= 1
      if jogador.vida < 1:
        print("="*100)
        print("")
        print("Game Over! VOCÊ PERDEU O GAME :(")
        cena()
        
        menu_temas(jogador)
      else:
        print("")
        print("Resposta incorreta, tente mais uma vez!")
        print("")
    
    elif escolha_entretenimento == 2 and escolha_entretenimento < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
    
  while True: #TEMA 1- PERGUNTA 3
    print("="*100)
    print("[Entreterimento]")
    print("")
    print("="*100)
    print("")
    print(f"Vida: {jogador.vida}")
    print(f"Moeda: {jogador.moeda}")
    print(f"Pulos Disponiveis: {jogador.pulo}")
    print("=" * 100)
    print("")
    print("[Pergunta 3]")
    print("")
    print("Quem é o criador da série de livros 'Harry Potter'?")
    print("")
    print("1) George R.R. Martin")
    print("2) Stephen King")
    print("3) J.K. Rowling")
    print("4) J.R.R. Tolkien")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    

    while True:
        try:
            escolha_entretenimento = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_entretenimento not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_entretenimento == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_entretenimento == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        break
    
    if escolha_entretenimento != 3 and escolha_entretenimento < 5:
      cena()
      jogador.vida -= 1
      if jogador.vida < 1:
        print("="*100)
        print("")
        print("Game Over! VOCÊ PERDEU O GAME :(")
        cena()
        
        menu_temas(jogador)
      else:
        print("")
        print("Resposta incorreta, tente mais uma vez!")
        print("")
    
    elif escolha_entretenimento == 3 and escolha_entretenimento < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
    
  while True: #TEMA 1 - PERGUNTA 4
    print("="*100)
    print("")
    print("[Entreterimento]")
    print("")
    print("="*100)
    print("")
    print(f"Vida: {jogador.vida}")
    print(f"Moeda: {jogador.moeda}")
    print(f"Pulos Disponiveis: {jogador.pulo}")
    print("=" * 100)
    print("")
    print("[Pergunta 4]")
    print("")
    print("Qual destes jogos foi desenvolvido pela empresa CD Projekt Red?")
    print("")
    print("1) The Elder Scrolls V: Skyrim")
    print("2) Dark Souls III")
    print("3) Stephen King")
    print("4) The Witcher 3: Wild Hunt")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    

    while True:
        try:
            escolha_entretenimento = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_entretenimento not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_entretenimento == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_entretenimento == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        break
    
    if escolha_entretenimento != 4 and escolha_entretenimento < 5:
      cena()
      jogador.vida -= 1
      if jogador.vida < 1:
        print("="*100)
        print("")
        print("Game Over! VOCÊ PERDEU O GAME :(")
        cena()
        
        menu_temas(jogador)
      else:
        print("")
        print("Resposta incorreta, tente mais uma vez!")
        print("")
    
    elif escolha_entretenimento == 4 and escolha_entretenimento < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
    
  while True: #TEMA 1 - PERGUNTA 5
    print("="*100)
    print("")
    print("[Entreterimento]")
    print("")
    print("="*100)
    print("")
    print(f"Vida: {jogador.vida}")
    print(f"Moeda: {jogador.moeda}")
    print(f"Pulos Disponiveis: {jogador.pulo}")
    print("=" * 100)
    print("")
    print("[Pergunta 5]")
    print("")
    print("Qual destes personagens não é um encanador famoso em jogos de vídeo?")
    print("")
    print("1) Mario")
    print("2) Luigi")
    print("3) Sonic")
    print("4) Wario")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")

    while True:
        try:
            escolha_entretenimento = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_entretenimento not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_entretenimento == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_entretenimento == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        break
    
    if escolha_entretenimento != 3 and escolha_entretenimento < 5:
      cena()
      jogador.vida -= 1
      if jogador.vida < 1:
        print("="*100)
        print("")
        print("Game Over! VOCÊ PERDEU O GAME :(")
        cena()
        
        menu_temas(jogador)
      else:
        print("")
        print("Resposta incorreta, tente mais uma vez!")
        print("")
    
    elif escolha_entretenimento == 3 and escolha_entretenimento < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      print("="*100)
      print("")
      print("<<PARABÉNS VOCÊ GANHOU!>>")
      print("")
      print("="*100)
      limpar_terminal()
      break






