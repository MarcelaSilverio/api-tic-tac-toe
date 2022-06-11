from http import HTTPStatus

class GameException(Exception):
    def __init__(self, msg):
        self.msg = msg

class WrongTurn(GameException):
	def __init__(self):
		super().__init__(msg="Turno inválido")
		self.status_code = HTTPStatus.BAD_REQUEST


class BoardNotFound(GameException):
	def __init__(self):
		super().__init__(msg="Tabuleiro não existe")
		self.status_code = HTTPStatus.NOT_FOUND

class InvalidPosition(GameException):
    def __init__(self):
        super().__init__(msg="Posição inválida")
        self.status_code = HTTPStatus.BAD_REQUEST
