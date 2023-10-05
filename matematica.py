from functions import mostrar_loja
from functions import cena
from functions import limpar_terminal
from functions import menu_temas

def matematica( jogador: object):
  jogador.vida = 3
  jogador.moeda = 0
  jogador.pulo = 0
  while True:
    print("="*100)
    print("")
    print("[Matemática]")
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
    print("Qual é a definição correta de derivada de uma função no ponto x?")
    print("")
    print("1) O valor médio da função em um intervalo em torno de x.")
    print("")
    print("2) A inclinação da reta tangente à curva da função no ponto x.")
    print("")
    print("3) A integral definida da função no ponto x.")
    print("")
    print("4) O valor mínimo da função no ponto x.")
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
    
    if escolha_programacao != 2 and escolha_programacao < 5:
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
    
    elif escolha_programacao == 2 and escolha_programacao < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break 
  
  while True: # TEMA 2 - PERGUNTA 2
    print("="*100)
    print("")
    print("[Matemática]")
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
    print("Qual é a notação correta para denotar a derivada de uma função f(x)?")
    print("")
    print("1) ∫f(x) dx")
    print("2) δf(x)")
    print("3) df(x)/dx")
    print("4) Σf'(x)")
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
    
    if escolha_programacao != 3 and escolha_programacao < 5:
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
    
    elif escolha_programacao == 3 and escolha_programacao < 5:
      print("")
      print("Resposta correta!! Você ganhou uma moeda!")
      jogador.moeda += 1
      cena()
      break
    
  while True: #TEMA 2- PERGUNTA 3
    print("="*100)
    print("[Matemática]")
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
    print("Qual é a derivada da função f(x) = 3x^2 - 2x + 1?")
    print("")
    print("1) f'(x) = nx^(n-1)")
    print("2) f'(x) = x^(n+1)")
    print("3) f'(x) = nx^n")
    print("4)  f'(x) = x^(n-1)")
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
    print("[Matemática]")
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
    print("Qual é a derivada da função trigonométrica f(x) = sin(x)?")
    print("")
    print("1) f'(x) = cos(x)")
    print("2) f'(x) = tan(x)")
    print("3)  f'(x) = sec(x)")
    print("4) f'(x) = -sin(x)")
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
      break
    
  while True: #TEMA 2 - PERGUNTA 5
    print("="*100)
    print("")
    print("[Matemática]")
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
    print("Qual é a derivada da função exponencial f(x) = e^x?")
    print("")
    print("1) f'(x) = e^x")
    print("2) f'(x) = 1")
    print("3) f'(x) = x*e^x")
    print("4)  f'(x) = 0")
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