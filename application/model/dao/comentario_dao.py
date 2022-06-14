from application.model.entity.estagiario_entity import Estagiario
from datetime import datetime

class ComentarioDAO:
    def __init__(self, nome, conteudo):
        self.id = 0
        self._data = datetime.now()
        self._curtidas = 0
        self.nome = nome
        self.conteudo = conteudo

    def incluirComentario(self):
        return lista_comentarios.append(self)

    def curtidas(self, curtidas):
        self._curtidas = curtidas
        self._curtidas += 1
        for like in range(len(self.nome, self.conteudo)):
            if self.nome[like].id and self.conteudo[like].id == self.id:
                self.nome[like], self.conteudo[like] = self._curtidas
                return self.nome, self.conteudo
        return None
    
    def horaDePostagem(self):
        return self._data.strftime("%d/%m/%Y %H:%M:%S")
    
    def get_id(self):
        return self.id
    
    def ordenarComentarios(self):
        return sorted(lista_comentarios, key=lambda comentario: comentario.id)

lista_comentarios = [
    ComentarioDAO('João', 'Primeiro comentário'),
    ComentarioDAO('Maria', 'Segundo comentário')
]