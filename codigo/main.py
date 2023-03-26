from codigo.bytebank import Funcionario

# jaezer = Funcionario('Jaezer', '17/12/2000', 2744)
# print(jaezer)


def teste_idade():
    funcionario_teste = Funcionario('Teste', '17/12/2000', 1222)
    print(f"Teste = {funcionario_teste.idade()}")

teste_idade()

