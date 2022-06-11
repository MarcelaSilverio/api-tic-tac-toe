from src.server.instance import server
from src.config.views import *

app, api = server.app, server.api

methods = ['GET', 'POST']

app.add_url_rule('/game', view_func=create_game, methods=["POST"])
app.add_url_rule('/game/status', view_func=get_board, methods=["GET"])
app.add_url_rule('/game/movement', view_func=play, methods=["POST"])

