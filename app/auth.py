"""
Configuração de autenticação
"""

usuario_valido = 'lauracarine'
senha_valida = "12345678"

def autenticar(usuario: str, senha: str) -> bool:
    if usuario == usuario_valido and senha == senha_valida:
        return True
    return False

