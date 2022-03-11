from src.controllers.board import *
from src.config.exceptions import *
from flask import request
import json
board_controller = BoardController()

def create_game():
	board = board_controller.create_board()

	return json.dumps({"id": board.id, "first_player": board.current_player})

def play():
	body = request.get_json()
	try:
		return json (board_controller.play(id=body["id"], player=body["player"],
         position=request.args.get("position")))
	except GameException as e:
		return json.dumps(e.msg), e.status_code

def get_board():
    try:
        return json.dumps(board_controller.get_board(id=request.args.get("id")))
    except GameException as e:
        return json.dumps(e.msg), e.status_code
