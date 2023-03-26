from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_17_12_2000_deve_retornar_23(self):
        entrada = '17/12/2000'  # GIVEN - Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()  # When - Ação

        assert resultado == esperado  # Then - Desfecho

    def test_quando_sobrenome_recebe_jaezer_lima_deve_retornar_lima(self):

        entrada = ' Jaézer Lima '
        esperado = 'Lima'

        jaezer = Funcionario(entrada, '17/12/2000', 1111)
        resultado = jaezer.sobrenome()

        assert resultado == esperado
