#classe que vai comandar tudo
class ContaCorrente():

     #funcao par criar conta, o que precisa
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0


#programa principal
#criar uma instancia da class ContaCorrente
conta_sivaldo = ContaCorrente("sivaldo", "111.222.333-44")

print(conta_sivaldo.nome)
print(conta_sivaldo.cpf)
print(conta_sivaldo.saldo)



