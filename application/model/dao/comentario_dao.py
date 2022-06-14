class ComentarioDAO:
    def __init__(self):
        self.__lista = []

    def incluirComentario(self, comentario):
        self.__lista.append(comentario)

    def curtidas(self, curtidas):
        self._curtidas = curtidas
        self._curtidas += 1
        for like in range(len(self.nome, self.conteudo)):
            if self.nome[like].id and self.conteudo[like].id == self.id:
                self.nome[like], self.conteudo[like] = self._curtidas
                return self.nome, self.conteudo
        return None
    
    def Lista(self):
        return self.__lista
