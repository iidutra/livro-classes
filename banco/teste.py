from cliente import Cliente
from conta import Conta, ContaEspecial
from banco_tatu import Banco

joao = Cliente("Joao da silva", "777-1234")
maria = Cliente("Maria silva", "777-2312")
jose = Cliente("Jose vargas", "123-3523")

conta1 = ContaEspecial([maria, joao], 2, 500, 1000)
conta1.deposito(500)
conta1.deposito(500)
conta1.saque(300)
conta1.extrato()

contaJM = Conta([joao, maria], 100)
contaJ = Conta([jose], 10)
tatu = Banco("Tatu")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()