class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        self.estado = None
    
    def __str__(self):
        return f"Cidade {self.nome}, {self.populacao}, {self.estado}"