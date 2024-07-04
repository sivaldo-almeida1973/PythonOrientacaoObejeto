#classe que vai comandar tudo
import time
from datetime import datetime
import pytz

class ContaCorrente():
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Attibutos:
         nome (str): Nome do Cliente
         cpf (str): CPF do Cliente
         agencia: Agencia do responsável pela conta
         num_conta:  Número da Conta Corrente do cliente
         saldo: Saldo disponivel na cona do cliente
         limite: Limite de cheque especial do cliente
         transações: Histórico de transações do cliente

    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now((fuso_BR))
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


     #funcao par criar conta, o que precisa
    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    #metodo consultar saldo
    def consultar_saldo(self):
        """
           Exibe o saldo atual da conta do cliente
           Não há parâmetros necessários.
        :return:
        """
        print(f"Seu saldo atual é de: R${self._saldo:,.2f}")

    def depositar(self, valor): #transacao------
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):    #metodo privado  _limite_conta(self) , para se usado somente dentro da classe
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor): #transacao----------
        if self._saldo -valor < self._limite_conta():
            print('Saldo insuficiente!')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print(f'Seu limite de Cheque especial é de: R${self._limite_conta():,.2f}')

    def consultar_historico_transacoes(self):
        print("Historico de Transações: ")
        print('Valor, Saldo, Dta e Hora')
        for transacao in self._transacoes:
            print(transacao)


    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito:
    def __init__(self, titular, conta_corrente):
        self.numero = 123
        self.titular = titular
        self.validade = None
        self.cod_seguranca = None
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self) # self pega toda instacnia da classe  CartaoCredito e adiciona em cartoes
        #conta_corrente._cartoes.append(self.numero) # self pega somente o numero e adiciona em cartoes




#programa principal
#criar uma instancia da class ContaCorrente
conta_sivaldo = ContaCorrente("sivaldo", "111.222.333-44", 222-34, 340)
cartao_sivaldo = CartaoCredito('Sivaldo', conta_sivaldo)
print(cartao_sivaldo.conta_corrente._num_conta)
print(cartao_sivaldo.titular)

print(conta_sivaldo._cartoes[0].numero)#indice 0 da classe CartaoCredito
