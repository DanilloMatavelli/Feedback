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
                    (nome, data_hora, comentario)
                VALUES
                    (%s, %s, %s)"""
        
        valores = (usuario, data_hora , mensagem)

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
        sql = """SELECT cod_comentario,
                        nome as usuario, 
                        data_hora,
                        curtidas,
                        comentario as mensagem
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
    
    def ultima_mensagem(usuario):
        # Criar conexão
        conexao = Conexao.criar_conexao()
        
        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor(dictionary=True)
        
        # Define a consulta SQL para buscar última mensagem do usuário
        sql = """
            SELECT cod_comentario,
                   nome as usuario,
                   data_hora,
                   curtidas,
                   comentario as mensagem
            FROM tb_comentarios
            WHERE nome = %s
            ORDER BY data_hora DESC
            LIMIT 1
        """
        
        valores = (usuario,)
        
         # Executando o comando SQL
        cursor.execute(sql, valores)
        
        # Pega a última mensagem
        resultado = cursor.fetchone()
        
        # Fecha a conexão
        cursor.close()
        conexao.close()
        
        return resultado
    
    # Pegar as mensagens e excluir do HTML
    def deletar_mensagem(codigo):
        # DELETANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a coneção 

        conexao = Conexao.criar_conexao()

        # O cursor será responsavel por manipular o banco de dados 
        cursor = conexao.cursor()

        # Criando o SQL que será executado para deletar o comentário
        sql = """DELETE FROM tb_comentarios
                 WHERE cod_comentario = %s"""
        
        # O valor do cod_comentario a ser deletado
        valores = (codigo,)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()

    # Pegar os likes do HTML
    def adicionar_curtida(codigo):
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular o banco de dados
        cursor = conexao.cursor()

        # Criando o SQL que será executado para adicionar uma curtida
        sql = """UPDATE tb_comentarios
                 SET curtidas = curtidas + 1
                 WHERE cod_comentario = %s"""
    
        # O valor do cod_comentario que será atualizado
        valores = (codigo,)

        # Executando o comando SQL
        cursor.execute(sql, valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o banco de dados
        cursor.close()
        conexao.close()
    
 # Pegar os likes do HTML
    def deletar_curtida(codigo):
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular o banco de dados
        cursor = conexao.cursor()

        # Criando o SQL que será executado para adicionar uma curtida
        sql = """UPDATE tb_comentarios
                 SET curtidas = curtidas - 1
                 WHERE cod_comentario = %s"""
    
        # O valor do cod_comentario que será atualizado
        valores = (codigo,)

        # Executando o comando SQL
        cursor.execute(sql, valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o banco de dados
        cursor.close()
        conexao.close()
    
