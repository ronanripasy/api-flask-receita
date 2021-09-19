import json
from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="templates")

bootstrap = Bootstrap(app)

def return_data(dias):
    return datetime.today() - timedelta(dias)

receitas = {
    "receitas": [
        {
            "nome": "Arroz com ovo",
            "tempo_de_preparo": 15,
            "serve_quantos": 10,
            "data": return_data(5).strftime("%d/%m/%Y")
        },
        {
            "nome": "Feijão ovo",
            "tempo_de_preparo": 45,
            "serve_quantos": 8,
            "data": return_data(7).strftime("%d/%m/%Y")
        },
        {
            "nome": "Pão com ovo",
            "tempo_de_preparo": 30,
            "serve_quantos": 5,
            "data": return_data(15).strftime("%d/%m/%Y")
        },
        {
            "nome": "Omelete",
            "tempo_de_preparo": 15,
            "serve_quantos": 2,
            "data": return_data(1).strftime("%d/%m/%Y")
        }
    ]
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/receita')
def lista_receitas():
    return jsonify(receitas)

@app.route('/receita/<int:id>')
def item_receita(id):
    try:
        lista_item = receitas['receitas']
        receita = lista_item[id - 1]
        return jsonify(receita)
    except IndexError as error:
        return 'Receita não encontrada'
    except Exception as e:
        return '404'


if __name__ == '__main__':
    app.run(debug=True)