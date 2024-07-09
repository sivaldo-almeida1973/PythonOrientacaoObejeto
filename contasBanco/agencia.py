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

class AgenciaComum(Agencia):
    pass


class AgenciaPremium(Agencia):
    pass



agencia1 = Agencia(22223333, 123546545, 4565)

agencia_virtual = AgenciaVirtual('www.agenciaVirtual.com.br', 22224444, 1520000000)
agencia_virtual.verificar_caixa()
print(agencia_virtual.caixa)









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
