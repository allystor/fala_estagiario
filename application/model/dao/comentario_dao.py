class ComentarioDAO:
    def __init__(self):
        self.__lista = []

    def incluirComentario(self, comentario):
        self.__lista.append(comentario)
    
    def Lista(self):
        return self.__lista
    
