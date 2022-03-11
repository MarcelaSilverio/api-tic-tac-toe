from board import *
from exceptions import *
from flask import request
import json

board_controller = BoardController()

def create_game(request):
	board = board_controller.create_board()

	return {"current_player": board.current_player, "id": board.id}

def play(request):
	try:
		board_controller.play(board_uuid=request.args.get("id"), player=request.args.get("player"))
	except GameException as e:
		return json(e.msg), e.status_code

def update_game(request):
    pass
