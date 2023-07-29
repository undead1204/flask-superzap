# Importa o flask
from flask import Flask, render_template
# Impota o websocket
from flask_socketio import SocketIO, send


# Instanciar o flask em um objeto 
app = Flask(__name__)

# Instanciar Socketio > Cria um tunel
socketio = SocketIO(app, cors_allowed_origins="*")

# Criar a funcionalidade de mandar mensagem
@socketio.on("message")
def grenciar_mensagem(mensagem):
    send(mensagem, broadcast=True) 

# Criar a rota
@app.route("/") # Decorator


def homepage():
    return render_template("index.html")


# Rodar o app
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80)
