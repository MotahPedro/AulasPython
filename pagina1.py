from flask import Flask, render_template #Importação necessária

app = Flask(__name__) #Instanciar objeto com flask

@app.route('/') #Definição de rota (Neste caso a rota raiz.)
def index(): # Função de nome index
    return 'Ola' #Conteúdo da rota

@app.route('/alunos')
def nova_rota_alunos():
    return "<h1>Pagina de alunos<h1>"

@app.route('/outrarota')
def outra():
    return "<p>Olha a tag HTML de paragrafo<p>" \
    "<img >"

app.run() #Comando de invocação do programa
