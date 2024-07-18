from classVendedor import Vendedor

#chama a classe
vendedor1 = Vendedor("sivaldo", )

#chama a funcao dentro da classe
vendedor1.vendeu(3000)
# vendedor1.calcular_bonus()


#chama a classe
vendedor2 = Vendedor('Lucas')
#chama a funcao dentro da classe
vendedor2.vendeu(5000)
# vendedor1.calcular_bonus()

#chama o atributo
print(vendedor1.nome, vendedor2.nome)
print(vendedor1.vendas, vendedor2.vendas)
print(vendedor1.bonus, vendedor1.bonus)

# Vantagens:
#
# Flexibilidade: Você pode adicionar validações ou processamento antes de definir o valor.
# Clareza: A lógica de definição de vendeu é separada da lógica de inicialização do objeto.
# Desvantagens:
#
# Complexidade: Requer uma chamada de função adicional para definir o valor.
# Conclusão
# A escolha entre essas abordagens depende das suas necessidades específicas. Se você precisa
# de simplicidade e não tem requisitos adicionais para a definição de vendeu, a primeira
# abordagem é suficiente. Se você precisa de mais controle e flexibilidade, a segunda
# abordagem com uma função pode ser mais adequada.
