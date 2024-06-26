# Criando nossa 1ª Classe em Python
# Sempre que você quiser criar uma classe, você vai fazer:
#
# class Nome_Classe:
#
# Dentro da classe, você vai criar a "função" (método) __init__
# Esse método é quem define o que acontece quando você cria uma instância da Classe
#
# Vamos ver um exemplo para ficar mais claro, com o caso da Televisão que a gente vinha comentando

#classes
class TV:
#sem o self não vai funcionar, fora da classe
#os parametros passados , são padrão
    def __init__(self):
        #atributos da tv
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = "Netflix"
        self.volume = 10

    #metodo mudar_canal , com parametro novo_canal
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal
        print(f'Canal alterado para {novo_canal}')


#programa

#instacias de TV
tv_sala = TV()
tv_quarto = TV()

#recebe mudar_canal, executar o metodo tem que ter (),com paramtro
tv_sala.mudar_canal("Globo")
tv_quarto.mudar_canal("Youtube")

#mudar cor tv_sala, mudar atributo não precisa ()
tv_sala.cor = "Azul"

print(tv_sala.canal)
print(tv_quarto.canal)
print(tv_sala.cor)

