class Main:
    pass
print("testando o projeto")

from Cliente import Cliente
from Conta import Conta

c1 = Cliente("andre carvalho gomes",32, 33001901995)
print("the name is",c1.nome_)

conta1 = Conta(c1,123,100)
print(conta1.saldo__)
print(conta1.titular__.get_nome())
print(conta1.titular__.get_age())
conta1.set_saldo(-100)
print(conta1.saldo__)