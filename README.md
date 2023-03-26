# Alura_ByteBank_TDD

Para executar os testes via terminal utilizar: pytest -v

A Tag -v serve para que o resultado do teste apareça de uma forma 'Verbosa'

A Tag -k é utilizada para filtrar por algum termo do nome do teste

A tag -m é para utilizar com mark, para utilizar como decorator

# Verificar Cobertura dos testes:

Utilizar o comando passando a pasta que vao estar sendo executados os testes: pytest --cov=codigo tests/
Para passar para mostrar os arquivos faltantes é : pytest --cov=codigo tests/ --cov-report term-missing 

