from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self):
        self.app = Flask("tic-tac-toe")
        self.api = Api(self.app,
            version = "1.0'",
            title = "tic-tac-toe API",
            description = "A simple multiplayer tic-tac-toe game",
            doc = "/docs"
        )
    
    def run(self):
        self.app.run()

server = Server()