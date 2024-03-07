from flask import Flask, render_template #Importação necessária

app = Flask(__name__) #Instanciar objeto com flask

@app.route('/') #Definição de rota (Neste caso a rota raiz.)
def index(): # Função de nome index
    return render_template('base.html') #Conteúdo da rota 1