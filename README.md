# Ping Pong #

Simples projeto academico com um cliente-servidor para trocar mensagens numa espécie de "ping-pong".

# Setup #

*   Utilize `python3+`.
*   Abra dois terminais.
*   Rode o servidor com `python server.py`.
*   Rode o cliente com `python client.py`.

Essa é uma amostra do que o projeto deve ser capaz de fazer:

| Terminal 1                | Terminal 2                |
|---------------------------|---------------------------|
| python server.py          | python client.py          |
| Esperando conexão.        | conectando-se ao servidor |
| Conectado                 | Conectado                 |
| Esperando mensagem        | Digite mensagem: lalala   |
|                           | Mensagem enviada          |
| Mensagem recebida: lalala | Esperando resposta        |
| Digite resposta: lelele   |                           |
| Resposta enviada.         | Resposta recebida: lelele |
|                           | Digite mensagem: SAIR     |
|                           | Desconectando.            |
| Conexão encerrada.        |                           |
