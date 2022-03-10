from src.server.instance import server
from uuid import uuid4
from random import choice

app, api = server.app, server.api


@app.route('/', methods=['GET'])
def home(): # Acho que não vai ter
    pass
    #renderizar home com opções ->
    # Criar nova partida
    # Entrar em uma partida Existente

@app.route("/game", methods=["POST"])
def createGame():
    """ Create a new game """
    first_symbol = choice(["X", "O"])
    game_id = uuid4()

    return {"id": game_id, "firstPlayer": first_symbol}

@app.route('/game/{id}', methods=['GET']) #talvez post tbm por conta do numero de jogadores
def enterGame():
    pass
    # Renderizar tabuleiro ->
    # Partida Inexistente
    # Arquivo com a situação atual da partida
    # Limitar a apenas dois jogadores

@app.route('/game/{id}/leave')
def leaveGame():
    pass
    # Jogo acaba


@app.route("/game/{id}/movement", methods=["POST"])
def movement():
    pass

    # Analisar movimento
    # Turno Errado
    # Chegamos ao Fim -> Velha ou Empate