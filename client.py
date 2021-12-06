import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

print("conectando-se ao servidor")
s.connect((host, port))
print("Conectado")

while True:
    text = input("\nDigite mensagem: ")
    s.send(text.encode())

    if text == 'SAIR':
        print("Desconectando.")
        break

    print("Mensagem enviada")

    data = s.recv(1024)
    print(f'Resposta recebida: {data.decode()}')