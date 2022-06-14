from application import app
from application.model.dao import ComentarioDAO
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    lista = ComentarioDAO.Lista()
    ordenar = sorted(lista, key=lambda comentario: comentario._data, reverse=True)
    return render_template('index.html',comentarios=ordenar)