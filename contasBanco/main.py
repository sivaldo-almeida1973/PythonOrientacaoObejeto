#programa principal
from contasBanco import ContaCorrente, CartaoCredito


#criar uma instancia da class ContaCorrente
conta_sivaldo = ContaCorrente("sivaldo", "111.222.333-44", 222-34, 340)
cartao_sivaldo = CartaoCredito('Sivaldo', conta_sivaldo)


print(cartao_sivaldo.titular)
print('Num Cartao',cartao_sivaldo.numero)

print("validade",cartao_sivaldo.validade)
print("codigo",cartao_sivaldo.cod_seguranca)


conta_sivaldo.nome = 'sivaldo vieira'
print(conta_sivaldo)

cartao_sivaldo.senha = '1256'
print(cartao_sivaldo.senha)

#consultar todos os valores da conta
print(conta_sivaldo.__dict__)
print(cartao_sivaldo.__dict__)
