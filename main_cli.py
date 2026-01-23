"""
Projeto de autenticação
"""

from app.auth import autenticar

def main():
    usuario = input("Informe seu nome de usuário: ")
    senha = input("Informe sua senha: ")

    if autenticar(usuario, senha):
        print("Acesso autorizado!")
    else:
        print("Usuário ou senha incorreto(a)")

if __name__ == "__main__":
    main()
