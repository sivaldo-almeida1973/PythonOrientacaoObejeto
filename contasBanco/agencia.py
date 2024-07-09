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

#herança-----------------------subclass
class AgenciaVirtual(Agencia):
    pass

class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass



agencia1 = Agencia(22223333, 123546545, 4565)

agencia_virtual = AgenciaVirtual(22224444, 1520000000, 1000)
agencia_virtual.caixa = 15000
agencia_virtual.verificar_caixa()


agencia_premium = AgenciaVirtual(22225555, 1520000000, 1234)
agencia_premium.caixa = 100000
agencia_premium.verificar_caixa()






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
