from asyncio import SubprocessProtocol
from datetime import time
import email
from itertools import repeat
from logging import error
from traceback import print_tb
from urllib import response
import pymysql
from flask import Flask,render_template, request, session ,flash ,url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import json
from flask import Response
import time
from werkzeug.utils import redirect
#connexao com banco
#senha new-password
app = Flask(__name__)
app.secret_key='123'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'lojaoff'
mysql = MySQL(app)
#
if app==True:
    print('ok')
else:
    print('erro')
leave_time = time.strftime("%H:%M:%S")
date_ = time.strftime("%d/%m/%Y")
#######################tela login


@app.route('/login')
def login():
    return render_template('loginsistema.html')

@app.route("/autenticar",methods=['GET', 'POST'])
def logar():
    try:  
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']

            session['usuario logado']=request.form['username']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM usuario WHERE nome = %s AND senha = %s', (username, password))
            # Fetch one record and return result
            account = cursor.fetchone()
            
            if account:

                return redirect('/menu')
            else:
                flash('A senha inserida está incorreta.')
           
            return redirect ('/login')
    except:
        print("erro login")

@app.route('/cadastrosistema', methods=['GET', 'POST'])
def cadadastronovo():
   
        if request.method == "POST":
            details = request.form
            nome = details['nome-cadastro']
            email= details['email-sistema']
            senha = details['senha-email']
        if nome=="" or email=="" or senha=="" :
            
            
            print('erro sistema')

        else:
            conexao = pymysql.connect(db='lojaoff', user='root', passwd='')

            cursor = conexao.cursor()
            
            cursor.execute("INSERT INTO  usuario (nome,senha,email)VALUES('{}','{}','{}')".format(nome,senha,email))
            conexao.commit()
            print("sucesso")
            return  "<h1>Cadast</h1>"
###############################################

@app.route('/cadastro')
def cadastro():
    return render_template('telassistema/cadastrocliente.html')
    
#carregar clientes e outra telas mysql
@app.route("/cadstroclientes",methods=['GET', 'POST'])
def cadastrocliente():
   
        try:
            if request.method == "POST":
                #id= render_template['id-cliente']
                details = request.form
                nome = details['nome'].upper()
                cpf_vs = details['cpf'].replace('.','').replace('-','').lstrip()
                endereco = details['end'].upper()
                cidade = details['cida-p'].upper().replace('.','').replace('-','').replace('(','').replace(')','').replace("'",' ').lstrip();
                estado = details['estado'].upper()
                celular = details['numero'].upper()
                ob_cliente = details['tx_mensagem'].upper()
                cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cur.execute("SELECT nome,cpf FROM clientes WHERE nome ='{}' and cpf ='{}'".format(nome,cpf_vs))
                resultado= cur.fetchall()
                
                if len(resultado):  #Verifica se o retorno contém alguma linha
                    return redirect(url_for("index"))  
                if nome=="" or endereco=="" or cpf_vs=="" or cidade=="" or estado=="" or   celular=="":
                    flash('A senha inserida está incorreta.')
                    
                    return redirect(url_for("index"))  
                    
                else:
                    conexao = pymysql.connect(db='lojaoff', user='root', passwd='')
                    cursor = conexao.cursor()
                    cursor.execute("INSERT INTO  clientes (nome, cpf,endereco, cidade, estado,  numero, obs_cliente)VALUES('{}','{}','{}','{}','{}','{}','{}')".format(nome,cpf_vs,endereco,cidade,estado,celular,ob_cliente))
                    conexao.commit()
                    ## redirect(url_for("index"))
                    #mensagem=("CADASTRO COM SUCESSO")
                    #if mensagem :
                       # return render_template("lista.html", msg=mensagem)
                    time.sleep(3)
                    return redirect(url_for("index"))   
        except:
           return"erro" 
        
@app.route('/menu')
def index():
    return render_template("menusistema.html")
#excluir clientes
@app.route("/excluir/<int:id>",methods=['GET', 'POST'])
def excluir(id):
    time.sleep(3)
    conexao = pymysql.connect(db='lojaoff', user='root', passwd='')
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM clientes WHERE id = {str(id)}")
    funcionarios = cursor.fetchall()
    conexao.commit()
    return redirect(url_for("show_map",funcionarios=funcionarios))
# carregar iframe
@app.route('/menu/tabelas')
def show_map():
    cur= mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT *FROM clientes")
    funcionario = cur.fetchall()
    print(funcionario)
    return render_template('tabelascliente.html', funcionarios=funcionario)
    
if __name__ == "__main__":
    app.run(debug=True)