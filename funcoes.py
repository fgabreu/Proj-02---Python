from time import sleep


#Cronometro - tempo(detalhe)
def tempo_cronometro(nome):
    print(f'{nome}....')
    cronometro = sleep(2)


#detalhe cabeçalho
def menu():
    print('=' * 60)

    print('\033[34mOLÁ, SEJA BEM VINDO A CADUNI (SISTEMA DE CADASTROS POCOBUS)\033[m')

    print('=' * 60)



#Menu Principal
def menu_principal():
    print('                   MENU INICIAL        ')
    menu_1 = int(input('''
        \033[1;36m[1] - CADASTRO (USUÁRIOS, CARTÃO, ÔNIBUS, MOTORISTA)
        [2] - DELETAR DADOS
        [3] - VISUALIZAÇÃO DE DADOS CADASTRADOS
        [4] - SAIR DO SISTEMA


        Digite sua opção:\033[m '''))
    return menu_1



#Menu Cadastro
def menu_cadastro():

    print('-' * 50)
    print(f'            MENU PARA CADASTRO        ')
    print('-' * 50)
    print('        ESCOLHA SUA OPÇÃO:      ')
    cadastro = int(input('''
        \033[1;33m[1] - USUÁRIO
        [2] - CARTÃO
        [3] - ÔNIBUS
        [4] - MOTORISTA
        [5] - RETORNAR

        Digite sua opção:\033[m '''))
        
    return cadastro



    

    






