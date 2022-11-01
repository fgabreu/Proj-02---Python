from time import sleep
from conexao import conectar_banco
import pandas as pd
import warnings

cursor, conn = conectar_banco()



def visualizar_usuario():
    print('DADOS TB USUÁRIO')
    print('Carregando....')
    cronometro = sleep(2) 
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)   
        tabela = pd.read_sql("SELECT * FROM  felipe_abreu.usuario",conn)
    
    print('*'*90)
    

    print(tabela)


    print('*'*90)
    

   

def visualizar_cartao():
    print('DADOS TB CARTÃO')
    print('Carregando....')
    cronometro = sleep(2)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        tabela = pd.read_sql("SELECT * FROM  felipe_abreu.cartao",conn)

    print('*'*90)
    

    print(tabela)


    print('*'*90)
    



def visualizar_onibus():
    print('DADOS TB ÔNIBUS')
    print('Carregando....')
    cronometro = sleep(2)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)   
        tabela = pd.read_sql("SELECT * FROM  felipe_abreu.onibus",conn)
    
    print('*'*90)
    

    print(tabela)


    print('*'*90)





def visualizar_motorista():
    print('DADOS TB MOTORISTA')
    print('Carregando....')
    cronometro = sleep(2)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)   
        tabela = pd.read_sql("SELECT * FROM  felipe_abreu.motorista",conn)

    print('*'*90)
    

    print(tabela)


    print('*'*90)
    
    