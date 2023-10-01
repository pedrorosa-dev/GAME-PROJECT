# CLEAR THE TERMINAL - LIMPAR TERMINAL
import os
def limpar_terminal():
    if os.name == 'posix':
        os.system('clear')  # Comando clear para sistemas Unix (MacOS e Linux)
    elif os.name == 'nt':
        os.system('cls')    # Comando cls para Windows
limpar_terminal()


#CREATE USER - CRIAR USUARIO
#USUARIO = JOGADOR
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 3  # Vida inicial fixa em 3

def cadastrar_usuario(nome):
    jogador = Jogador(nome)
    return jogador

