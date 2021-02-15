class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
    
    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)
    
    def populacao(self):
        return sum([c.populacao for c in self.cidades])