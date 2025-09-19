import pyodbc

def obter_conexao():
    # define os parametros de conexao
    driver   = '{ODBC Driver 17 for SQL Server}'
    servidor = '.\SQLEXPRESS'
    banco    = 'cursos_superiores'
    usuario  = 'sa'
    senha    = '12345' # poder ser também: "senha", "senha@123", "Senha@123"


    # realiza conexao com o BD
    string_conexao = f'Driver={driver};Server={servidor};Database={banco};UID={usuario};PWD={senha}'
    conexao = pyodbc.connect(string_conexao)
    
    # retorna a conexao  
    return conexao

def executar_sql(sql, commit=True):
    '''Executa um comando SQL no BD (geralmente um INSERT, UPDATE ou DELETE)'''
    # obtem conexao
    conexao = obter_conexao()
    # cria um cursor() e executa o SQL informado
    ret = conexao.cursor().execute(sql)
    # verifica se eh para efetivar as modificações no BD
    if commit:
        conexao.commit()
    # retorna o resultado do metodo execute()
    return ret 


def executar_select(sql, retornar_cursor=False):
    '''Executa um comando SELECT no BD e retorna os registros'''
    # obtem conexao
    conexao = obter_conexao()
    # cria um cursor(), executa o SELECT informado e traz os todos os registros
    cursor = conexao.cursor()
    ret = cursor.execute(sql).fetchall()
    # retorna os registros do BD
    if not retornar_cursor:
        return ret 
    else:
        return ret, cursor




