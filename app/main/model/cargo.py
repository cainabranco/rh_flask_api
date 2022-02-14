from .. import db


class Cargo(db.Model):
    """" Model de Cargo para armazenar os dados relacionados"""
    __tablename__ = 'cargos'

    id_cargo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cargo = db.Column(db.String(55), unique=True, nullable=False)
    descricao = db.Column(db.String(255))
    colaboradores = db.relationship('Colaborador', backref='cargos', lazy=True)
