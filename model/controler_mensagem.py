from data.conexao import Conexao
import datetime

class Mensagem:
    
    def cadastrarmensagem(usuario,mensagem):
        data_hora = datetime.datetime.today()

        # CADASTRANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a coneção 

        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor()

        # Criando o SQL que será executado 
        sql = """INSERT INTO tb_comentarios
                    (nome, comentarios, data_hora)
                VALUES
                    (%s, %s, %s)"""
        
        valores = (usuario, mensagem, data_hora)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()
    
    # Pegar as mensagens e fazer aparecer no HTML
        
    def recuperar_mensagens():
        # Criar conexão
        conexao = Conexao.criar_conexao()
        
        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor(dictionary = True)
        
        # Define a consulta SQL
        sql = """SELECT nome as usuario, 
                        comentarios as mensagem,
                        data_hora
                 FROM tb_comentarios"""
                 
        # Executando o comando SQL
        cursor.execute(sql)
        
        # Pegas os resultados do usuario e aparecer no HTML
        # Recuperando os dados e guardando em uma variavel
        resultado = cursor.fetchall()
        
        # Fecha a conexão com o banco
        cursor.close()
        conexao.close()
        
        return resultado



        