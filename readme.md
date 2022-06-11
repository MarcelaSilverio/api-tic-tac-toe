# TIC-TAC-TOE API
> API de jogo multiplayer de Jogo da Velha feita em Flask Python
![](header.png)

## Instalação

- Crie um ambiente virtual Python
- Instale os pacotes presentes no arquivo requirements.txt
- Rode o arquivo main.py


Linux:

```sh
virtualenv env

source env/bin/activate

pip3 install -r requirements.txt

python3 main.py
```

Windows:

- Siga os mesmos passos anteriores, porém com comandos referentes ao sistema operacional Windows

## Exemplo de uso

Para poder utilizar a API utilize uma ferramenta similar ao Postman: https://www.postman.com

As requisições serão feitas como no exemplo a seguir:

```sh
http://127.0.0.1:5000/game/movement?id=1b0f053d-1876-47a2-ac5d-4707547438aa
```

