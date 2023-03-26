from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_17_12_2000_deve_retornar_23(self):
        entrada = '17/12/2000'  # GIVEN - Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When - Ação

        assert resultado == esperado  # Then - Desfecho
