from flask import request
from src.server.instance import server
from uuid import uuid4
from random import choice

app, api = server.app, server.api
games = []


@app.route("/game", methods=["POST"])
def createGame():
    """ Create a new game """

    global games
    symbol = choice(["X", "O"])
    new_id = True

    while new_id:
        new_id = False
        game_id = str(uuid4())
        for game in games:
            if game_id in game:
                new_id = True

    games.append([game_id, symbol, [[0]*3]*3])
    return {"id": game_id, "firstPlayer": symbol}


@app.route("/game/situation", methods=["GET"])
def gameSituation(id=None):
    """ Send the game situation """
    
    global games
    id = request.args.get("id")
    exist = False

    for game in games:
        if id in game:
            return {"turno": game[1], "tabuleiro": game[2]}
        
    return {"msg": "Partida não encontrada"}


@app.route("/game/movement", methods=["POST"])
def movement():
    
    global games
    id = request.args.get("id")

    for game in games:
        if id in game:           
            body = request.get_json()  

            if game[1] != body["player"]:
                return {"msg": "Não é turno do jogador"}
            elif game[2][body["tabuleiro"]["y"]-2][body["tabuleiro"]["x"]] == 1:   
                return {"msg": "Posição indisponível"}
            else:
                game[2][body["tabuleiro"]["y"]-2][body["tabuleiro"]["x"]] = 1
                
                if  game[1] == "X":
                    game[1] = "O"
                else:
                    game[1] = "X"
                
                return {"código": "200"}
            
        
    return {"msg": "Partida não encontrada"}
    
    # Analisar movimento
    # Turno Errado
    # Chegamos ao Fim -> Velha ou Empate