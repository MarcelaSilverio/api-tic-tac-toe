from uuid import uuid4
from random import choice
from exceptions import *
from enum import Enum

class BoardController():
	def __init__(self):
		self.boards = {} #  {"uuid": "board_object"}

	def create_board(self):
		new_board = Board()
		self.boards[new_board.uuid] = new_board

		return new_board

	def play(self, board_uuid, player):
		try:
			return self.boards[board_uuid].play(player)
		except IndexError:
			raise BoardNotFound()

	def is_finished(self, board_uuid):
		pass

	def get_board(self, board_uuid):
		return self.boards[board_uuid].get_board()

class BoardStatus(str, Enum):
	FINISHED = "finished"
	RUNNING = "running"


class Board():
    def __init__(self):
        self.id = uuid4()
        self.symbols = ["X", "O"]
        self.current_player =  choice(self.symbols)
        self.board = [[0]*3]*3
        self.blanks = 9
        self.status = BoardStatus.RUNNING

    def play(self, player, position):
        if self.current_player != player:
            raise WrongTurn
        elif self.board[abs(position.y - 2)][position.x] != 0:
            raise InvalidPosition
        else:
            self.board[position.y - 2][position.x] = self.current_player
            self.blanks -= 1
            
            # Rows and columns
            for position in range(3):
                if self.board[0][position] == self.board[1][position] == self.board[2][position] != 0:
                    self.status = BoardStatus.finished
                    return {"msg": "Partida finalizada", "winner": self.current_player}
                
                elif self.board[position][0] == self.board[position][1] == self.board[position][2] != 0:
                    self.status = BoardStatus.finished
                    return {"msg": "Partida finalizada", "winner": self.current_player}

            # Diagonal
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
                    self.status = BoardStatus.finished
                    return {"msg": "Partida finalizada", "winner": self.current_player}
            elif self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
                    self.status = BoardStatus.finished
                    return {"msg": "Partida finalizada", "winner": self.current_player}
            elif self.blanks == 0:
                    self.status = BoardStatus.finished
                    return {"msg": "Partida finalizada", "winner": "Draw"}
            else:
                self.current_player = (self.symbols.copy.remove(self.current_player))[0]
                return self.get_board()
            

    def is_finished(self):
        return self.status == BoardStatus.FINISHED

    def get_board(self):
        return {"board": self.board, "status": self.status}


