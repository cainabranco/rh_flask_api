from .. import db


class Lider(db.Model):
    """ Model de Líder para armazenar os dados de relacionados a lideres"""
    __tablename__ = 'lideres'

    id_lider = db.Column(db.Integer, primary_key=True, autoincrement=True)
    matricula_lider = db.Column(db.Integer, db.ForeignKey('colaboradores.matricula'), unique=True, nullable=False)
    colaboradores = db.relationship('Colaborador', backref='lideres', lazy=True)
