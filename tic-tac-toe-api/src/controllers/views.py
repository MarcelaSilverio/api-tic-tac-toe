from board import *
from exceptions import *
import json

board_controller = BoardController()

def create_game(request):
	board = board_controller.create_board()

	return json({"id": board.id, "first_player": board.current_player})

def play(request):
	try:
		return json (board_controller.play(board_uuid=request.args.get("id"), player=request.args.get("player"),
         position=request.args.get("position")))
	except GameException as e:
		return json(e.msg), e.status_code

def get_board(request):
    try:
        return json(board_controller.get_board(board_uuid=request.args.get("id")))
    except GameException as e:
        return json(e.msg), e.status_code
