from estado import Estado
from cidades import Cidade

am = Estado("Amazonas", "AM")
am.adiciona_cidade(Cidade("Manaus", 1861838))
am.adiciona_cidade(Cidade("Parintins", 103828))

sp = Estado("São paulo", "SP")
sp.adiciona_cidade(Cidade("São paulo", 11376685))
sp.adiciona_cidade(Cidade("Guarulhos", 1244518))

for estado in [am, sp]:
    print(f"Estado: {estado.nome}, Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome}, Populacao: {cidade.populacao}")
    print(f"Populacao do Estado: \n {estado.populacao()}")