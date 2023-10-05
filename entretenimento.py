from functions import mostrar_loja
from functions import cena
from functions import limpar_terminal
from functions import menu_temas



#TEMA - ENTRETEIRIMENTO -FUN - TEMA 1 - 1 PERGUNTA

def entretenimento( jogador: object):
  jogador.vida = 3
  jogador.moeda = 0
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
        cena()
        break #passar para proxima pergunta
    
    if escolha_entretenimento != 1 and escolha_entretenimento < 5:
      cena()
      jogador.vida -= 1
      if jogador.vida < 1:
        print("="*100)
        print("")
        print("Game Over! VOCÊ PERDEU O GAME :(")
        print("="*100)
        print("")
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
        cena()
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
        cena()
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
        cena()
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