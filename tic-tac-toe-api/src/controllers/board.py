from uuid import uuid4
from random import choice
from exceptions import *
from enum import Enum

class BoardController():
	def __init__(self):
		self.boards = {} #  {"uuid": "board_object"}

	def create_board(self) -> Board:
		new_board = Board()
		self.boards[new_board.uuid] = new_board

		return new_board

	def play(self, board_uuid, player):
		# board existe?
		# board está ativa?
		try:
			self.boards[board_uuid].play(player)
		except IndexError:
			raise InvalidBoard()

	def is_finished(self, board_uuid):
		pass

    def update(self, board_uuid):
        self.boards[board_uuid].board

class BoardStatus(str, Enum):
	FINISHED = "finished"
	RUNNING = "running"


class Board():
	def __init__(self):
		self.id = uuid4()
		self.current_player =  choice(["X", "O"])
		self.board = [[0]*3]*3
		self.status = BoardStatus.RUNNING

	def play(self, player):
		# é a vez do player?
		pass

	def is_finished(self):
	    return self.status == BoardStatus.FINISHED

    def oi(self):
	    return self.status == BoardStatus.FINISHED



