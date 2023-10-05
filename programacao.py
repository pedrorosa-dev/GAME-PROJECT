from functions import mostrar_loja
from functions import cena
from functions import limpar_terminal
from functions import menu_temas


def programacao(jogador: object):
  jogador.vida = 3
  jogador.moeda = 0
  jogador.pulo = 0
  while True:
    print("="*100)
    print("")
    print("[Programação]")
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
    print("Qual é a palavra-chave utilizada para definir um função em Python?")
    print("")
    print("1) Create")
    print("2) Function")
    print("3) Def")
    print("4) make")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    
    
    while True:
        try:
            escolha_programacao = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_programacao not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_programacao == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_programacao == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        cena()
        break #passar para proxima pergunta
    
    if escolha_programacao != 3 and escolha_programacao < 5:
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
    
    elif escolha_programacao == 3 and escolha_programacao < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break 
  
  while True: # TEMA 2 - PERGUNTA 2
    print("="*100)
    print("")
    print("[Programação]")
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
    print("Qual alternativa representa um tipo de dado que não é considerado primitivo em Python?")
    print("")
    print("1) int")
    print("2) str")
    print("3) list")
    print("4) func")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    

    while True:
        try:
            escolha_programacao = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_programacao not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_programacao == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_programacao == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        cena()
        break
    
    if escolha_programacao != 4 and escolha_programacao < 5:
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
    
    elif escolha_programacao == 4 and escolha_programacao < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
    
  while True: #TEMA 2- PERGUNTA 3
    print("="*100)
    print("[Programação]")
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
    print("Qual operador é utilizado para comparar igualdade entre valores em Python?")
    print("")
    print("1) ==")
    print("2) =")
    print("3) !=")
    print("4) <>")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    

    while True:
        try:
            escolha_programacao = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_programacao not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_programacao == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_programacao == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        break
    
    if escolha_programacao != 1 and escolha_programacao < 5:
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
    
    elif escolha_programacao == 1 and escolha_programacao < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
    
  while True: #TEMA 2 - PERGUNTA 4
    print("="*100)
    print("")
    print("[Programação]")
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
    print("Em um sistema de gerenciamento de banco de dados relacional (RDBMS), qual tipo de relacionamento representa uma\n associação entre duas tabelas em que um registro em uma tabela está associado a vários registros em outra tabela?")
    print("")
    print("Qual das opções reprsenta o tipo de relacionamento mencionado acima em um banco de dados relacional?")
    print("")
    print("1) Relacionamento de um para um (1:1)")
    print("")
    print("2) Relacionament de muitos para um (N:1)")
    print("")
    print("3) Relacionamento de um para muitos (1:M)")
    print("")
    print("4) Relacionamento de muitos para muitos (M:M)")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")
    

    while True:
        try:
            escolha_programacao = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_programacao not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_programacao == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_programacao == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        cena()
        break
    
    if escolha_programacao != 4 and escolha_programacao < 5:
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
    
    elif escolha_programacao == 4 and escolha_programacao < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
    
  while True: #TEMA 2 - PERGUNTA 5
    print("="*100)
    print("")
    print("[Programação]")
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
    print("Qual é a principal diferença entre listas e tuplas em Python?")
    print("")
    print("1)  Listas são mutáveis, enquanto tuplas são imutáveis.")
    print("2) Listas podem conter elementos de diferentes tipos, enquanto tuplas só podem conter elementos do mesmo tipo.")
    print("3) Listas são indexadas por números inteiros, enquanto tuplas são indexadas por strings.")
    print("4)  Listas têm uma ordem fixa, enquanto tuplas podem ser reordenadas dinamicamente.")
    print("="*100)
    print("")
    print("<<5>> LOJA")
    print("<<6>> PULAR")
    print("")
    print("=" * 100)
    print("")

    while True:
        try:
            escolha_programacao = int(input("Digite de 1 a 6 para escolher uma opção: "))
            print("="*100)
            if escolha_programacao not in [1, 2, 3, 4, 5 , 6]:
                raise ValueError
            break  # Sai do loop se o número válido for digitado
        except ValueError:
            print("")
            print(f"Erro: apenas de 1 a 6.")
            print("")
    if escolha_programacao == 5:
        print("")
        print("Entrando...")
        cena()
        mostrar_loja(jogador)

    if escolha_programacao == 6:
      if jogador.pulo < 1:
        print("")
        print("Não há pulos disponíveis no momento...")
        cena()
      else:
        jogador.pulo -=1
        cena()
        break
    
    if escolha_programacao != 1 and escolha_programacao < 5:
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
    
    elif escolha_programacao == 1 and escolha_programacao < 5:
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
