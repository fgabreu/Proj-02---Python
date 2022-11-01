import pyodbc

#conexão do python com o Banco de Dados

def conectar_banco():
    server = 'sql-estudo.database.windows.net'
    driver = '{ODBC Driver 17 for SQL Server}'
    database = 'db-estudos'
    username = 'felipe.abreu@blueshift.com.br'
    Authentication='ActiveDirectoryInteractive'
    port = '1433'
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';PORT='+port+';DATABASE='+database+';UID='+username)#+';PWD='+password)

    cursor = conn.cursor()

    return cursor, conn

