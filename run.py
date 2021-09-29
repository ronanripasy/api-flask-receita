from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify, request
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api
from receitas.models import Pessoa

app = Flask(__name__, template_folder="templates")
bootstrap = Bootstrap(app)
api = Api(app)

class PessoaView(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoa.query.filter_by(nome=nome).first()
            response = {
                'nome': pessoa.nome,
                'email': pessoa.email,
                'id': pessoa.id
            }
        except Exception as e:
            response = {
                "status": "erro",
                "mensagem": "Pessoa não encontrada"
            }
        return response

    def put(self, nome):
        pessoa = Pessoa.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        
        if 'email' in dados:
            pessoa.email = dados['email']
        pessoa.save()

        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'email': pessoa.email
        }
        return response

api.add_resource(PessoaView, '/pessoa/<string:nome>/')


def return_data(dias):
    return datetime.today() - timedelta(dias)

receitas = [
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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/receita', methods=['GET', 'POST'])
def receita():
    data = {}
    if request.method == 'POST':
        receita = request.json
        receitas.append(receita)
        data = receitas
    elif request.method == 'GET':
        data = receitas
    return jsonify(data)

@app.route('/receita/<int:id>')
def item_receita(id):
    try:
        receita = receitas[id - 1]
        return jsonify(receita)
    except IndexError as error:
        return 'Receita não encontrada'
    except Exception as e:
        return '404'

if __name__ == '__main__':
    app.run(debug=True)