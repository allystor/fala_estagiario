from application.model.dao import ComentarioDAO
from datetime import datetime 


class Estagiario:
    
    def __init__(self, nome, conteudo):
        self._data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.id = len(ComentarioDAO.Lista()) + 1
        self._curtidas = 0
        self.nome = nome
        self.conteudo = conteudo
        self.curtidas = self._curtidas
    
    def get_nome(self):
        return self.nome

    def get_conteudo(self):
        return self.conteudo
    
