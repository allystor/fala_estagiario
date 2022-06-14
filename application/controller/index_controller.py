from crypt import methods
from application import app
from application.model.dao.comentario_dao import ComentarioDAO
from application.model.entity.estagiario_entity import Estagiario
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    comentario = ComentarioDAO.ordenarComentarios()
    return render_template('index.html',comentario=comentario)