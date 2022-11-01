
from time import sleep
from conexao import conectar_banco
import pyodbc

cursor, conn = conectar_banco()



def cadastrar_usuario():
    print('CADASTRO DE USUÁRIO')
    nome = str(input('Digite o seu nome: ')).upper().strip()
    sobrenome = str(input('Digite o seu Sobrenome: ')).upper().strip()
    email = str(input('Digite o seu email: ')).strip()
    bairro = str(input('Digite o seu Bairro: ')).upper().strip()
    data_nascimento = input('Digite a sua data de nascimento (yyyy-mm-dd): ').strip()

    comando = f""" INSERT INTO felipe_abreu.usuario(NOME, SOBRENOME, EMAIL, BAIRRO, DATA_NASCIMENTO)
    VALUES 
        ('{nome}', '{sobrenome}', '{email}', '{bairro}', '{data_nascimento}') """
    cursor.execute(comando)
    cursor.commit()

    print('Cadastrando....')
    cronometro = sleep(2)
    print('\033[1;33mUSUÁRIO CADASTRADO COM SUCESSO\033[m')
    



def cadastrar_cartao():
    print('CADASTRO DE CARTÃO')
    id_proprietario = int(input('Digite o ID do proprietario: '))
    credito = float(input('Informe a quantidade de créditos: '))
    tipo = str(input('Informe o tipo: ')).upper().strip()
    data_emissao = input('Digite a data de emissão (yyyy-mm-dd): ').strip()

    comando = f""" INSERT INTO felipe_abreu.cartao(ID_PROPRIETARIO, QTDE_CREDITOS, CATEGORIA, EMISSAO)
    VALUES 
        ('{id_proprietario}',' {credito}', '{tipo}', '{data_emissao}') """
    cursor.execute(comando)
    cursor.commit()
  
    print('Cadastrando....')
    cronometro = sleep(2)
    print('\033[1;33mCARTÃO CADASTRADO COM SUCESSO\033[m')




def cadastrar_onibus():
    print('CADASTRO DE ÔNIBUS')
    num_placa = str(input('Digite a placa: ')).upper().strip()
    num_linha = int(input('Digite o n° da linha: '))
    modelo_onibus = str(input('Digite o modelo: ')).strip()
    data_fabricacao = input('Digite o ano de fabricação (yyyy): ').strip()
    id_motorista = int(input('Digite o ID do motorista: '))

    comando = f""" INSERT INTO felipe_abreu.onibus(NUM_PLACA, NUM_LINHA, MODELO_ONIBUS, ANO_FABRICACAO, ID_MOTORISTA)
    VALUES 
        ('{num_linha}', '{num_linha}', '{modelo_onibus}', '{data_fabricacao}', '{id_motorista}') """
    cursor.execute(comando)
    cursor.commit()

    print('Cadastrando....')
    cronometro = sleep(2)
    print('\033[1;33mÔNIBUS CADASTRADO COM SUCESSO\033[m')




def cadastrar_motorista():
    print('CADASTRO DE MOTORISTA')
    numero_cnh = int(input('Digite o número da CNH: '))
    nome = str(input('Digite o seu Nome: ')).upper().strip()
    sobrenome = str(input('Digite o seu Sobrenome: ')).upper().strip()
    data_nascimento = input('Digite a sua data de nascimento (yyyy-mm-dd): ').strip()

    comando = f""" INSERT INTO felipe_abreu.motorista(NUM_CNH, NOME, SOBRENOME, DATA_NASCIMENTO)
    VALUES 
        ('{numero_cnh}', '{nome}', '{sobrenome}', '{data_nascimento}') """
    cursor.execute(comando)
    cursor.commit()

    print('Cadastrando....')
    cronometro = sleep(2)
    print('\033[1;33mMOTORISTA CADASTRADO COM SUCESSO\033[m')