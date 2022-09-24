from flask import Flask, render_template

app = Flask(__name__)

lista_usuarios = ['Leonardo' , 'Thamyres', 'Gabriel']

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/contato")
def contato():
    return render_template('contato.html')


@app.route("/usuarios")
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route("/login")
def login():
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)