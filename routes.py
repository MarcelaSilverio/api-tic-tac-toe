from flask import Flask

app = Flask("Jogo Da Velha")

@app.route('', methods=['GET'])
def home(): # Acho que não vai ter
    pass
    #renderizar home com opções ->
    # Criar nova partida
    # Entrar em uma partida Existente

@app.route("/game", methods=["POST"])
def createGame():
    
    return {"id": game_id, "firstPlayer": first_symbol}
    #Gerar um id
    #Definir o simbolo

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
    # Turno Errado
    # Chegamos ao Fim -> Velha ou Empate


app.run()