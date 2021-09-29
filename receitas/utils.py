from datetime import date
from faker import Faker
from models import Receita
from provider import ReceitaProvider

def insere_receita_faker():
    fake = Faker()
    fake.add_provider(ReceitaProvider)

    for _ in range(61):
        receita = Receita(titulo=fake.receita_titulo(), descricao=fake.text(max_nb_chars=20), data=fake.date_between(start_date='-5y', end_date='today'))
        receita.save()

def insere_receita():
    receita = Receita(titulo='Feijão ovo', descricao='Feijão ovo um sabor sem igual', data=date.today())
    receita.save()

def all_receitas():
    receitas = Receita.query.all()
    for i in receitas:
        print(i.titulo)
    # print(receitas)

def filtra_receita(filtro):
    try:
        receita = Receita.query.filter(Receita.titulo.like(f'%{filtro}%'))
        print(f'{receita[0].titulo} - {receita[0].descricao}')
    except Exception as e:
        print('Nenhum receita encontrada')

def altera_pessoa(filtro, data):
    try:
        receita = Receita.query.filter_by(titulo=filtro).first()
        receita.descricao = 'Esse arroz foi editado.'
        receita.save()
    except Exception as e:
        print('Receita não encontrada para edição')

def delete_pessoa(id):
    receita = Receita.query.filter_by(id=id).first()
    receita.delete()

if __name__ == '__main__':
    # insere_receita()
    # delete_pessoa(1)
    all_receitas()
    # filtra_receita('Arroz')
    # altera_pessoa('Arroz com ovo', 'Esse arroz foi editado.')
    # insere_receita_faker()