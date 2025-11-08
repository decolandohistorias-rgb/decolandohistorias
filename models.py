from db import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(50), unique=True)
    nome = db.Column(db.String(30), nullable=False)
    senha = db.Column(db.String(), nullable=False)
    profile_cor = db.Column(db.String(), nullable=True)

class Flights(db.Model):
    __tablename__ = 'flights'
        
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    departure = db.Column(db.String())
    arrival = db.Column(db.String())
    departure_iata = db.Column(db.String(3))
    arrival_iata = db.Column(db.String(3))
    number = db.Column(db.String())
    date = db.Column(db.String())
    tempo_voo = db.Column(db.String())
    horario_saida = db.Column(db.String())
    horario_chegada = db.Column(db.String())
    terminal = db.Column(db.String())
    gate = db.Column(db.String())
    id = db.Column(db.Integer, primary_key=True)

class Settings(db.Model):
    __tablename__ = 'settings'
        
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    mostrar_sem_voos = db.Column(db.Boolean)
    mostrar_tabela = db.Column(db.String)
    mostrar_botao_logout = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)

class Family(db.Model):
    __tablename__ = 'family'

    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    pessoas = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)


