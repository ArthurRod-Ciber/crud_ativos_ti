class EntidadeBase:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

    def transformar_em_dict(self):
        return {'id': self.id}
    