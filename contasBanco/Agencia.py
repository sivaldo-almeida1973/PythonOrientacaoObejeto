from random import randint

class Agencia:
  #metodo de inicializacao
    def __init__(self, telefone, cnpj, numero_ag):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero_ag = numero_ag
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa Atual: {}'. format(self.caixa))
        else:
            print('Valor do caixa OK. Caixa Atual: {} '.format(self.caixa))


    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))

#herança-----------------------subclass herda da super classe
class AgenciaVirtual(Agencia):
    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)# chama o init da super classe
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj , numero_ag=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
       def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj , numero_ag=randint(1001, 9999))
        self.caixa = 10000000

       def adicionar_cliente(self, nome, cpf, patrimonio):
           if patrimonio > 1000000:
               super(AgenciaPremium, self).adicionar_cliente(nome, cpf, patrimonio)
           else:
               print('O cliente não possui o patrimônio minimo para entrar nesta agência Premium!')


if __name__ == '__main__':  #impede de rodar o codigo abaixo, quando for chamado no main

    agencia1 = Agencia(22223333, 123546545, 4565)

    agencia_virtual = AgenciaVirtual('www.agenciaVirtual.com.br', 22224444, 1520000000)
    agencia_virtual.verificar_caixa()
    # print(agencia_virtual.caixa)
    # print(agencia_virtual.site)


    agencia_comum = AgenciaComum(22225555, 2550000000)
    # agencia_comum.verificar_caixa()

    agencia_premium = AgenciaPremium(222226666, 55500000000)
    # agencia_premium.verificar_caixa()

    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)


    agencia_premium.adicionar_cliente('lice', 1450000000, 10000001)
    print(agencia_premium.clientes)


    agencia_comum.adicionar_cliente('Sivaldo', 10000000000, 100)
    print(agencia_comum.clientes)
    # agencia1.caixa = 100000000
    #
    # agencia1.verificar_caixa()
    #
    # agencia1.emprestar_dinheiro(1500, 12345678912, 0.02)
    # print(agencia1.emprestimos)
    #
    # #adicionar cliente
    # agencia1.adicionar_cliente('Lucas', 123456789012, 10000)
    # print(agencia1.clientes)
