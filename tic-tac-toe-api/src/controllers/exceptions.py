from flask import http

class GameException(Exception):
	pass

class WrongTurn(GameException):
	def __init__(self):
		super().__init__(msg="Turno inválido")
		self.status_code = http.HTTPStatus.BAD_REQUEST


class BoardNotFound(GameException):
	def __init__(self):
		super().__init__(msg="Tabuleiro não existe")
		self.status_code = http.HTTPStatus.NOT_FOUND