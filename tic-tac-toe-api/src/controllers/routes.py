from src.server.instance import server
import views

app, api = server.app, server.api

app.add_url_rule('/game', view_func=views.create_game)
app.add_url_rule('/game/<id>', view_func=views.update_game)
app.add_url_rule('/game/<id>/movement', view_func=views.play)


# @app.route("/game", methods=["POST"]) #criar arquivos de rota separado, criar classe -> board
# def createGame():
#     """ Create a new game """

#     global games
#     symbol = choice(["X", "O"])
#     new_id = True

#     while new_id:
#         new_id = False
#         game_id = str(uuid4())
#         for game in games:
#             if game_id in game:
#                 new_id = True

#     games.append([game_id, symbol, [[0]*3]*3])
#     return {"id": game_id, "firstPlayer": symbol} # deixar json 


# @app.route("/game/situation", methods=["GET"])
# def gameSituation(id=None):
#     """ Send the game situation """
    
#     global games
#     id = request.args.get("id")
#     exist = False

#     for game in games:
#         if id in game:
#             return {"turno": game[1], "tabuleiro": game[2]}
        
#     return {"msg": "Partida não encontrada"}


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

                winner = False
                
                if  game[1] == "X":
                    game[1] = "O"
                else:
                    game[1] = "X"

                # Rows
                if game[2][0][0] == 1 and game[2][0][1] == 1 and game[2][0][2] == 1:
                    winner = True
                if game[2][1][0] == 1 and game[2][1][1] == 1 and game[2][1][2] == 1:
                    winner = True
                if game[2][2][0] == 1 and game[2][2][1] == 1 and game[2][2][2] == 1:
                    winner = True

                # Columns
                if game[2][0][0] == 1 and game[2][1][0] == 1 and game[2][2][0] == 1:
                    winner = True
                if game[2][0][1] == 1 and game[2][1][1] == 1 and game[2][2][1] == 1:
                    winner = True
                if game[2][0][2] == 1 and game[2][1][2] == 1 and game[2][2][2] == 1:
                    winner = True

                # Diagonals
                if game[2][0][0] == 1 and game[2][1][1] == 1 and game[2][2][2] == 1:
                    winner = True
                if game[2][2][0] == 1 and game[2][1][1] == 1 and game[2][0][2] == 1:
                    winner = True

                if winner:
                    return {"status": "Partida finalizada", "winner": body["player"]}
                else:
                    return {"código": "200"}
            
        
    return {"msg": "Partida não encontrada"}
    
    # Analisar movimento
    # Turno Errado
    # Chegamos ao Fim -> Velha ou Empate