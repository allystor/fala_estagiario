from application import app
from application.model.dao.estagiario_dao import EstagiarioDAO
from application.model.entity.estagiario_entity import Estagiario
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comentar', methods=['POST','GET'])
def comentar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        comentario = request.form.get('comentario')
        estagiarioDAO = EstagiarioDAO(nome, comentario)
        if EstagiarioDAO:
            return estagiarioDAO.listarPostagens()
        return "Erro ao comentar"

@app.route('/curtidas', methods=['POST','GET'])
def curtidas():
    if request.method == 'POST':
        id = request.form.get('id')
        estagiarioDAO = EstagiarioDAO()
        if not EstagiarioDAO:
            return "Erro ao curtir"
        return  estagiarioDAO.listarPostagens()