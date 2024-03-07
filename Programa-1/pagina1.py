from flask import Flask, render_template #Importação necessária

app = Flask(__name__) #Instanciar objeto com flask

@app.route('/') #Definição de rota (Neste caso a rota raiz.)
def index(): # Função de nome index
    return render_template('base.html') #Conteúdo da rota 1

@app.route('/sobre')
def rota_sobre():
    return render_template('sobre.html') #Conteúdo da rota 2

@app.route('/servicos')
def rota_servicos():
    return render_template('servicos.html') #Conteúdo da rota 3

@app.route('/contato')
def rota_contato():
    return render_template('contato.html') #Conteúdo da rota 4

@app.route('/conteudo')
def rota_conteudo():
    return render_template('conteudo.html')

app.run() #Comando de invocação do programa
