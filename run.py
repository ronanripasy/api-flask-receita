from flask import Flask, json, render_template, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="templates")

bootstrap = Bootstrap(app)

receitas = {
    "receitas": [
        {
            "nome": "Arroz com ovo",
            "tempo_de_preparo": 15,
            "serve_quantos": 10
        },
        {
            "nome": "Feijão ovo",
            "tempo_de_preparo": 45,
            "serve_quantos": 8
        },
        {
            "nome": "Pão com ovo",
            "tempo_de_preparo": 30,
            "serve_quantos": 5
        },
        {
            "nome": "Omelete",
            "tempo_de_preparo": 15,
            "serve_quantos": 2
        }
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/receitas')
def lista_receitas():
    return jsonify(receitas)


if __name__ == '__main__':
    app.run(debug=True)