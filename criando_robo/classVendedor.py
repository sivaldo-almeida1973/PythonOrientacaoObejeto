# A diferença entre definir o atributo vendeu diretamente no construtor (__init__) e criar uma função para definir esse valor está na flexibilidade e controle que você tem sobre como e quando o valor é atribuído. Vamos explorar as duas abordagens:
#
# 1. Definindo vendeu no Construtor
# No seu exemplo atual, você está definindo vendeu diretamente no construtor:
#
# Python

class Vendedor():

    def __init__(self, nome_vendedor, vendeu):
        self.nome = nome_vendedor
        self.vendas = vendeu
        self.meta = 500
        self.bonus = 0


# Vantagens:
#
# Simplicidade: É direto e fácil de entender.
# Inicialização: O valor de vendeu é definido no momento da criação do objeto.
# Desvantagens:
#
# Menos flexível: Se você precisar validar ou processar o
# valor de vendeu antes de atribuí-lo, você terá que adicionar essa lógica
# no construtor, o que pode torná-lo mais complexo.


# 2. Usando uma Função para Definir vendeu
# Outra abordagem seria criar uma função para definir o valor de vendeu:


class Vendedor():

    def __init__(self, nome_vendedor):
        self.nome = nome_vendedor
        self.vendas = 500
        self.meta = 500
        self.bonus = 0

    def vendeu(self, quantidade_vendas):
          # Aqui você pode adicionar validações ou processamento
        self.vendas = quantidade_vendas
        self.calcular_bonus()  #chama a funcao calcular_bonus()

    def calcular_bonus(self):
        if self.vendas > self.meta:
            self.bonus = 30
        else:
            self.bonus = 0

# E então, você pode definir o valor de vendeu após a criação do objeto:

