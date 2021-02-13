from cliente import Cliente
from contas import Conta
from banco import Banco

joao = Cliente("Joao", "555-7123")
maria = Cliente("Maria da silva", "667-2312")
jose = Cliente("Jose", "555-1234")
contaJM = Conta([joao, maria], 100)
contaJ = Conta([jose], 10)
tatu = Banco("Tatu")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)

print(lista_contas())