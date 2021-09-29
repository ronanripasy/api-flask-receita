from datetime import date
from faker import Faker
from models import Receita, Pessoa
from provider import ReceitaProvider

def insere_receita_faker():
    fake = Faker()
    fake.add_provider(ReceitaProvider)

    for _ in range(61):
        receita = Receita(titulo=fake.receita_titulo(), descricao=fake.text(max_nb_chars=20), data=fake.date_between(start_date='-5y', end_date='today'))
        receita.save()

def insere_pessoa():
    fake = Faker()
    for _ in range(30):
        pessoa = Pessoa(nome=fake.first_name(), email=fake.email())
        pessoa.save()

if __name__ == '__main__':
    insere_pessoa()