from src.server.instance import server
import views

app, api = server.app, server.api

app.add_url_rule('/game', view_func=views.create_game)
app.add_url_rule('/game/<id>', view_func=views.update_game)
app.add_url_rule('/game/<id>/movement', view_func=views.play)

