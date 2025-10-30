class Conta:
    def __init__ (self, titular, numero, saldo):
        self.saldo__ = 0
        self.numero__ = numero
        self.titular__ = titular

    def get_saldo(self):
        return self.saldo__

    def set_saldo(self,saldo):
        if (saldo < 0 ):
            print(" o saldo não pode ser negativo")
        else:
            self.saldo__ = saldo

    def get_numero(self):
        return self.numero__

    def set_numero(self,numero):
        self.numero__ = numero

    def get_titular(self):
        return self.titular__

    def set_titular(self,titular):
        self.titular__ = titular