class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    
    def resumo(self):
        print(f"CC número: {self.numero} Saldo: {self.saldo:10.2f}")
        
        for cliente in self.clientes:
            print(f"Nome: {cliente.nome} Telefone: {cliente.telefone}")
    
    def pode_sacar(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])
    
    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print (f"\n  Saldo: {self.saldo:10.2f}\n")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
    
    def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            return False
        
    def extrato(self):
        Conta.extrato(self)
        print(f"\n Limite: {self.limite}")
        print(f"\n Disponível: {self.limite + self.saldo}")