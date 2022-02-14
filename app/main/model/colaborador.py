from .. import db, flask_bcrypt
from datetime import datetime


class Colaborador(db.Model):
    """ Model de Colaborador para armazenar os dados relacionados"""
    __tablename__ = 'colaboradores'

    matricula = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False)
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargos.id_cargo'), nullable=False)
    id_lider = db.Column(db.Integer, db.ForeignKey('lideres.id_lider'))
    email = db.Column(db.String(255), unique=True, nullable=False)
    data_inclusao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    status = db.Column(db.String(50), nullable=False, default='ATIVO')
    senha_hash = db.Column(db.String(100))
    salario = db.Column(db.Float(asdecimal=True), nullable=False)
    lideres = db.relationship('Lider', backref='colaboradores', lazy=True)

    @property
    def senha(self):
        raise AttributeError('password: write-only field')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = flask_bcrypt.generate_password_hash(senha).decode('utf-8')

    def checa_senha(self, senha):
        return flask_bcrypt.check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f"<Colaborador '{self.nome}'>"