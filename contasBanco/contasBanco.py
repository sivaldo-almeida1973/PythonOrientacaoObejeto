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
    def __init__(self, nome, cpf, conta, agencia):
        self._nome = nome
        self._cpf = cpf
        self._conta = conta
        self._agencia = agencia
        self._saldo = 0
        self._limite = None
        self._transacoes = []

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

#programa principal
#criar uma instancia da class ContaCorrente
conta_sivaldo = ContaCorrente("sivaldo", "111.222.333-44", 222-34, 340)

print(f'Cliente: {conta_sivaldo._nome}')
print(f'CPF: {conta_sivaldo._cpf}')
print(f'Conta: {conta_sivaldo._conta}')
print(f'Agência: {conta_sivaldo._agencia}')

conta_sivaldo.consultar_saldo()

#depositar dinheiro
conta_sivaldo.depositar(10000)
conta_sivaldo.consultar_saldo()

time.sleep(3)  #ver diferença de tempo (10 segundo)
#sacar dinheiro
conta_sivaldo.sacar_dinheiro(500)

print("saldo final")
conta_sivaldo.consultar_saldo()

conta_sivaldo.consultar_limite_cheque_especial()

print('-'*29)
conta_sivaldo.consultar_historico_transacoes()

print('-'*29)
#criar contacorrente da mae
conta_mae = ContaCorrente("Maria", "333.222.444-44", 235, 2345)
#tranferir valor do sivaldo para a mae
conta_sivaldo.transferir(1000, conta_mae)

print('-'*29)
conta_sivaldo.consultar_saldo()
conta_mae.consultar_saldo()

print('-'*29)
conta_sivaldo.consultar_historico_transacoes()
print('-'*29)
conta_mae.consultar_historico_transacoes()

help(ContaCorrente)
