from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

PORT = 8000

USUARIO_AUTORIZADO = "lauracarine"
SENHA_AUTORIZADA = "12345678"


class MeuHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/login.html":
            self.path = "/login.html"
            return super().do_GET()
        else:
            return super().do_GET()

    def do_POST(self):
        if self.path == "/index.html":
            # Lê tamanho do corpo da requisição
            length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(length).decode('utf-8')

            # Faz parse dos dados do formulário
            data = parse_qs(post_data)
            usuario = data.get("usuario", [""])[0]
            senha = data.get("senha", [""])[0]

            if usuario == USUARIO_AUTORIZADO and senha == SENHA_AUTORIZADA:
                # Redireciona para a página principal
                self.path = "/index.html"
                return super().do_GET()
            else:
                # Login incorreto → responde direto com HTML
                self.send_response(401)
                self.send_header("Content-type", "text/html")
                self.end_headers()

                # HTML completo com botão Home
                erro_html = f"""
                <!DOCTYPE html>
                <html lang="pt-BR">
                <head>
                    <meta charset="UTF-8">
                    <title>Erro de Login</title>
                </head>
                <body>
                    <h1>Usuário ou senha incorreto(a)</h1>
                    <form action="/login.html" method="get">
                        <input type="submit" value="Home">
                    </form>
                </body>
                </html>
                """
                self.wfile.write(erro_html.encode('utf-8'))

server = HTTPServer(("0.0.0.0", PORT), MeuHandler)
print(f"Servidor rodando na porta {PORT}")
server.serve_forever()

"""server = HTTPServer(("0.0.0.0", PORT), SimpleHTTPRequestHandler)
print(f"Servidor rodando na porta {PORT}")

server.serve_forever()"""