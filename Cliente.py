class Cliente:
    def __init__(self, nome, age, fone):
        self.nome_ = nome
        self._age = age
        self._fone = fone

    def set_nome(self, nome):
        self.nome_ = nome

    def get_nome(self):
        return self.nome_

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def get_fone(self):
        return self._fone

    def set_fone(self,fone):
        self._fone = fone


