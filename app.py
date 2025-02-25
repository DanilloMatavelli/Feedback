from flask import Flask, render_template, request, redirect
import datetime
import mysql.connector

app = Flask(__name__)

lista_mensagem = [

]



# AQUI IRÁ TODAS AS MINHAS ROTAS
@app.route("/")
def pagina_inicial():
    # Para escrever na página HTML
    return render_template ("pagina_inicial.html")

# Rota para pegar dados do HTML É POST para Mandar pro HTML é GET
@app.route("/post/mensagem" , methods = ["POST"])
def post_mensagem():

    # Para pegar o campo do úsuario no HTML
    # Peguei as informações vinda do formulario
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mansagem")
    data_hora = datetime.datetime.today()

    # CADASTRANDO AS INFORMAÇÕES NO BANCO DE DADOS
    # Criando a coneção 

    conexao = mysql.connector.connect(
        host = "localhost", port = 3306,
        user = "root",
        password = "root",
        database = "feedback"
    )

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
    

    # Redireiona para a pagina inicial
    return redirect("/")


# Para iniciar o app
app.run(debug=True)