from application import app
from application.model.dao import ComentarioDAO
from application.model.entity.estagiario_entity import Estagiario
from flask import request,render_template, redirect, url_for

@app.route('/comentar', methods=['POST','GET'])
def comentar():
    nome = request.form.get('nome', 'none')
    conteudo = request.form.get('conteudo', 'none')
    comentario = Estagiario(nome, conteudo)
    ComentarioDAO.incluirComentario(comentario)
    if ComentarioDAO:
        return render_template('index.html', comentario=ComentarioDAO.Lista())
    else:
        return 'Erro ao postar comentario!'

