from application.model.entity.estagiario_entity import Estagiario
import datetime

class EstagiarioDAO:
    def __init__(self):
        self.__id = 0
        self.__data = datetime.datetime.now()
        self.__curtidas = 0
        self.__estagiarios = []

    def listarPostagens(self):
        return self.__estagiarios

    def curtidas(self):
        self.__curtidas += 1
        for like in range(len(self.__estagiarios)):
            if self.__estagiarios[like].id == self.__id:
                self.__estagiarios[like] = (self.__curtidas)
        return None
    
    def horaDePostagem(self):
        return self.__data.strftime("%d/%m/%Y %H:%M:%S")
    
    def get_id(self):
        return self.__id