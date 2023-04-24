# Proj-02---Python
Projeto 02 - Python 

Objetivo: Desenvolver o sistema de cartão de transporte  municipal e o sistema que controlará a frota. Para desenvolver esse sistema utilizaremos programação orientada a objetos. O seu algoritmo deverá armazenar todos os dados dentro do banco de dados SQL Server. As classes e seus atributos já foram pré-definidos. Todos os atributos deverão ser privados, portanto será necessário criar métodos gets e sets para todas as classes.

Definição das classes:

Usuário
- ID: int
- Nome: string
- Sobrenome: string
- E-mail: string
- Bairro: string
- Data de nascimento: date

Cartão
- ID do cartão: int
- ID do proprietário: int
- Quantidade de créditos disponível: double (comum, estudante, vale-transporte ou idoso): string
- Data de emissão: date

Ônibus
- Número da placa: int
- Número da linha: int
- Modelo do ônibus: string
- Ano de fabricação: date
- ID motorista: int

Motorista
- ID motorista: int
- Número CNH: int
- Nome: string
- Sobrenome: stirng
- Data de nascimento: date


To do

No SQL Server conectado com o BD no Azure, crie uma tabela para cada classe, conforme orientações acima.
Após a criação das tabelas, desenvolver o sistema em Python levando em consideração as orientações acima para classes e suas entidades e a conexão com o banco.
Crie uma interface no terminal para que o usuário possa cadastrar e visualizar as informações.
