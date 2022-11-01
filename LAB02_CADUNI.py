from funcoes import tempo_cronometro, menu, menu_cadastro, menu_principal
from imput_dados import cadastrar_usuario, cadastrar_cartao, cadastrar_motorista, cadastrar_onibus
from deletar_dados import deletar_cartao, deletar_motorista, deletar_onibus, deletar_usuario
from visualizar_dados import visualizar_cartao, visualizar_usuario, visualizar_motorista, visualizar_onibus
from conexao import conectar_banco

cursor, conn = conectar_banco()

# Menu
menu()

while True:
    menu_1 = menu_principal()
# opções de escolha menu
    if menu_1 == 1:
        tempo_cronometro('Carregando')
        while True:
            cadastro = menu_cadastro()
#OPÇÕES DE ESCOLHA USUÁRIO
            if cadastro == 0 or cadastro > 5:
                print('\033[31mOPÇÃO INVÁLIDA. ESCOLHA UMA OPÇÃO DE 1 A 5.\033[m')
                #cadastro = funçao cadastro(criar)
            elif cadastro == 1:
                tempo_cronometro('Carregando')
                cadastrar_usuario()                
            elif cadastro == 2:
                tempo_cronometro('Carregando')
                cadastrar_cartao()
            elif cadastro == 3:
                tempo_cronometro('Carregando')
                cadastrar_onibus()
            elif cadastro == 4:
                tempo_cronometro('Carregando')
                cadastrar_motorista()
            else:
                tempo_cronometro('Retornando ao Menu Inicial')
                break
#DELETAR DADOS    
    if menu_1 == 2:
        tempo_cronometro('Carregando')
        while True:
            cadastro = menu_cadastro()
            if cadastro == 0 or cadastro > 5:
                print('\033[31mOPÇÃO INVÁLIDA. ESCOLHA UMA OPÇÃO DE 1 A 5.\033[m')
            elif cadastro == 1:
                deletar_usuario()                
            elif cadastro == 2:
                deletar_cartao()
            elif cadastro == 3:
                deletar_onibus()
            elif cadastro == 4:
                deletar_motorista()
            else:
                tempo_cronometro('Retornando ao Menu Inicial')
                break
#VISUALIZAR DADOS      
    if menu_1 == 3:
        tempo_cronometro('Carregando')
        while True:
            cadastro = menu_cadastro()
            if cadastro == 0 or cadastro > 5:
                print('\033[31mOPÇÃO INVÁLIDA. ESCOLHA UMA OPÇÃO DE 1 A 5.\033[m')
            elif cadastro == 1:
                visualizar_usuario()                
            elif cadastro == 2:
                visualizar_cartao()
            elif cadastro == 3:
                visualizar_onibus()
            elif cadastro == 4:
                visualizar_motorista()
            else:
                tempo_cronometro('Retornando ao Menu Inicial')
                break
#ENCERRANDO O SISTEMA      
    if menu_1 == 4:
        tempo_cronometro('Finalizando o Sistema...')
        break

print('\033[1;34mA CADUNI DESEJA VOCÊ UM BOM DIA\033[m')



