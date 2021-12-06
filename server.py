import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)

while True:
    print("Esperando conexão.")
    c, addr = s.accept()
    print("Conectado")

    while True:
        data = c.recv(1024)
        if data.decode() == 'SAIR':
            print("Conexão encerrada.")
            break

        print(f'\nMensagem recebida: "{data.decode()}"')

        text = input("Digite resposta: ")
        c.send(text.encode())
        print("Resposta enviada")