class EntidadeBase:
    def __init__(self, id):
        self.id = id

    def transformar_em_dict(self):
        return {'id': self.id}
