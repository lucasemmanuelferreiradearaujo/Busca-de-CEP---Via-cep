import requests

class BaseDeDados:
    def __init__(self):
        self.arquivo = open('cep.txt', 'r')
        self.listacep = list()
        self.listainformacao = []

    def criar_lista_cep(self):
        for valor in self.arquivo:
            aux = str(valor).strip('\n')
            self.listacep.append(aux)

    def busca_informacao(self):
        for valor in self.listacep:
            self.resultadoDadosCep = requests.get(f'https://viacep.com.br/ws/{valor}/json/').json()
            self.formarta_dados()
            self.escrever_base_dados()
            self.dataframe.close()
            self.apagar_lista()


    def formarta_dados(self):
        cont = 0
        for chave in self.resultadoDadosCep:
            cont += 1
            if cont < 3:
                if self.resultadoDadosCep[chave] not in '':
                    self.listainformacao.append(self.resultadoDadosCep[chave])
                else:
                    break

    def escrever_base_dados(self):
        self.dataframe = open('resultado.txt','a')
        cont = 0
        for valor in self.listainformacao:
            cont +=1
            if cont < len(self.listainformacao):
                self.dataframe.writelines(valor+'\t')
            else:
                self.dataframe.writelines(valor+'\n')

    def apagar_lista(self):
        self.listainformacao.clear()

db = BaseDeDados()
db.__init__()
db.criar_lista_cep()
db.busca_informacao()
db.formarta_dados()
