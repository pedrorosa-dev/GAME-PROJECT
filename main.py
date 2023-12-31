# TENTEI OTIMIZAR OS CODIGOS SEPARANDO POR ARQUIVO MAS NAO DEU!
import time 
import sys
from functions import limpar_terminal, cadastrar_usuario, tempo_resposta, cena, menu_temas
# MENU LOGIN
# Dicionário para armazenar nomes de usuário e senhas
banco_usuarios = {}
logado = False  # Variável para controlar se o usuário está logado
bem_vindo_nome_usuario = None  # criado para nao alterar o nome na hora de exibir o seja bem vindo 

while True:
    print("=" * 100)
    print("")
    if logado and bem_vindo_nome_usuario:
        print(f"Seja bem-vindo, {bem_vindo_nome_usuario}")
        print("")
    print("Menu:")
    print("")
    print("1 - Fazer login")
    print("2 - Registrar")
    print("3 - Entrar no jogo")
    print("4 - Sair do jogo")
    print("")
    print("=" * 100)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Fazer login - made a login
        print("")
        try:
          nome_usuario = input("Digite o nome de usuário: ")
          if not nome_usuario.strip():
            raise ValueError
          
          senha = input("Digite a senha: ")
          if not senha.strip():
            raise ValueError
          if nome_usuario in banco_usuarios and banco_usuarios[nome_usuario] == senha: #checa se o nome do usuario esta no dicionario
              print("")
              print("Login bem-sucedido!")
              logado = True #Agora é possivel entrar no jogo
              bem_vindo_nome_usuario = nome_usuario  # faz com que exiba o seja bem vindo
              cena()
          else:
              print("")
              print("Nome de usuário ou senha incorretos.")
              logado = False
              cena()
        except ValueError:
          print("")
          print("ERRO: NÃO PODE ESPAÇO VAZIO")
          cena()
          
    elif opcao == "2":
        # Registrar - register
        print("")
        try:
          nome_usuario = input("Digite um nome de usuário: ")
          if not nome_usuario.strip(): #TIRA O ESPACO EM BRANCO CASO O USUARIO FACA LOGIN SEM DIGITAR NADA
            raise ValueError
          
          senha = input("Digite uma senha: ") # tira o espaco em BRANCO CASO A SENHA NAO ESTEJA DIGITADA
          if not senha.strip():
            raise ValueError
          if nome_usuario in banco_usuarios: # Checa se o nome de usuario esta no dicionario
              print("")
              print("Nome de usuário já existe. Escolha outro.") 
              cena()
          else:
              banco_usuarios[nome_usuario] = senha
              print("")
              print("Registro bem-sucedido!")
              cena()
        except ValueError: #EXIBIR O ERRO DO ESPACO VAZIO NA HORA DE REGISTRAR O USUARIO E A SENHA
          print("")
          print("ERRO: NÃO PODE ESPAÇO VAZIO")
          cena()  
          
    elif opcao == "3":
        # Entrar no jogo - join in the game caso o logado esteja True
        if logado:
            print("")
            print("Entrando...")
            limpar_terminal()
            break
        else:
            print("")
            print("Você precisa fazer login para entrar no jogo.")
            cena()
            
    elif opcao == "4":
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

# INTRODUCTION - INTRODUÇÃO
print('=' * 100)
print("")
print("<<<PEYTRON QUIZ>>>")
print("")
print("")
print("Bem-vindo ao Peytron Quiz! Teste suas habilidades em programação, entretenimento e matemática.")
print("")
print('=' * 100)
time.sleep(1.4)
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
        cena()
        if not nome_jogador.strip():#.strip para tirar os espacos
            raise ValueError
        jogador = cadastrar_usuario(nome_jogador)
        break  # Sai do loop se um nome válido for digitado
    except ValueError:
        print("")
        print(f"Erro: Por favor, digite um nome válido.")
        print("")
        
print("=" *100)
print("")
print("")

print(f"Olá, {jogador.nome}! Vamos começar nossa jornada? Espero que esteja pronto, porque o caminho não será nada fácil!")
print("")
print("")
print("=" *100)
tempo_resposta()
print("")
print("Carregando...")
limpar_terminal()

#INICIO DO GAME
menu_temas(jogador)