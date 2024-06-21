#classe que vai comandar tudo
class ContaCorrente():

     #funcao par criar conta, o que precisa
    def __init__(self, nome, cpf, conta, agencia):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta
        self.agencia = agencia
        self.saldo = 0
        self.limite = None

    #metodo consultar saldo
    def consultar_saldo(self):
        print(f"Seu saldo atual é de: R${self.saldo:,.2f}")

    def depositar(self, valor):
        self.saldo += valor

    def _limite_conta(self):    #metodo privado  _limite_conta(self) , para se usado somente dentro da classe
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo -valor < self._limite_conta():
            print('Saldo insuficiente!')
            self.consultar_saldo()
        else:
            self.saldo -= valor

    def consultar_limite_cheque_especial(self):
        print(f'Seu limite de Cheque especial é de: R${self._limite_conta():,.2f}')

#programa principal
#criar uma instancia da class ContaCorrente
conta_sivaldo = ContaCorrente("sivaldo", "111.222.333-44", 222-34, 340)

print(f'Cliente: {conta_sivaldo.nome}')
print(f'CPF: {conta_sivaldo.cpf}')
print(f'Conta: {conta_sivaldo.conta}')
print(f'Agência: {conta_sivaldo.agencia}')

conta_sivaldo.consultar_saldo()

#depositar dinheiro
conta_sivaldo.saldo= 10000
conta_sivaldo.consultar_saldo()

#sacar dinheiro
conta_sivaldo.sacar_dinheiro(10500)

print("saldo final")
conta_sivaldo.consultar_saldo()

conta_sivaldo.consultar_limite_cheque_especial()


