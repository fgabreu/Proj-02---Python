from time import sleep
from conexao import conectar_banco
import pyodbc

cursor, conn = conectar_banco()


def deletar_usuario():
    print('DELETAR DADOS DE USUÁRIO')
    id = str(input('Digite o ID do usuário que deseja deletar: ')).upper().strip()
        
    comando = (f""" DELETE FROM felipe_abreu.usuario
                WHERE ID = ? """)
    cursor.execute(comando, id) 
    cursor.commit()

    print('Deletando....')
    cronometro = sleep(2)
    print('\033[1;33mDADOS DELETADOS COM SUCESSO\033[m')
    



def deletar_cartao():
    print('DELETAR DADOS DE CARTÃO')
    id_cartao = int(input('Digite o ID do cartão: '))

    comando = (f""" DELETE FROM felipe_abreu.cartao
                WHERE ID_CARTAO = ? """)
    cursor.execute(comando, id_cartao)
    cursor.commit() 
  
    print('Deletando....')
    cronometro = sleep(2)
    print('\033[1;33mDADOS DELETADOS COM SUCESSO\033[m')




def deletar_onibus():
    print('DELETAR DADOS ÔNIBUS')
    num_placa = str(input('Digite a placa: ')).upper().strip()

    comando = (f""" DELETE FROM felipe_abreu.onibus
                WHERE NUM_PLACA = ?""")
    cursor.execute(comando, num_placa)
    cursor.commit()
    
    print('Deletando....')
    cronometro = sleep(2)
    print('\033[1;33mDADOS DELETADOS COM SUCESSO\033[m')




def deletar_motorista():
    print('DELETAR DADOS DO MOTORISTA')
    numero_cnh = int(input('Digite o número da CNH: '))

    comando = (f""" DELETE FROM felipe_abreu.usuario
                WHERE NUM_CNH = ?""")
    cursor.execute(comando, numero_cnh)
    cursor.commit()  

    print('Deletando....')
    cronometro = sleep(2)
    print('\033[1;33mDADOS DELETADOS COM SUCESSO\033[m')


