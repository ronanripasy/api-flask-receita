from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///receitas.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Receita(Base):
    __tablename__ = 'receitas'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(40))
    descricao = Column(Text)
    data = Column(Date)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def __repr__(self) -> str:
        return '<Receita {}>'.format(self.titulo)

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()