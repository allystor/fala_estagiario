
class Estagiario:
    def __init__(self,nome,comentario):
        self.__nome = nome
        self.__comentario = comentario
    
    def get_nome(self):
        return self.__nome

    def get_comentario(self):
        return self.__comentario
