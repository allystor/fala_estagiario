from application import app
from application.model.dao.comentario_dao import ComentarioDAO
from application.model.entity.estagiario_entity import Estagiario
from flask import request,render_template

@app.route('/comentar', methods=['POST'])
def comentar():
    nome = request.form['nome']
    conteudo = request.form['conteudo']
    comentario = ComentarioDAO(nome, conteudo)
    ComentarioDAO.incluirComentario(comentario)
    if ComentarioDAO:
        return render_template('index.html', comentario=comentario)
    else:
        return 'Erro ao postar comentario!'

@app.route('/curtidas', methods=['POST'])
def curtidas():
    id = request.args['id']
    comentario = ComentarioDAO.get_id(id)
    if not comentario:
        return 'Comentario não encontrado', 404
    comentario = ComentarioDAO.curtidas()
    if not comentario:
        return 'Erro curtir comentario', 500
    return 200