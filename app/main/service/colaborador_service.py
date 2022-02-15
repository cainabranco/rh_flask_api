from app.main import db
from app.main.model.colaborador import Colaborador


def salva_novo_colaborador(data):
    colaborador = Colaborador.query.filter_by(email=data['email']).first()

    if not colaborador:
        novo_colaborador = Colaborador(
            nome=data['nome'],
            sobrenome=data['sobrenome'],
            id_cargo=data['id_cargo'],
            id_lider=data['id_lider'],
            email=data['email'],
            senha=data['senha'],
            salario=data['salario'],
        )

        salva_mudancas(novo_colaborador)
        response_object = {
            'status': 'success',
            'message': 'Cadastro bem sucedido.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Colaborador já cadastrado.',
        }
        return response_object, 409


def get_all_colaboradores():
    return Colaborador.query.all()


def get_colaborador(matricula):
    return Colaborador.query.filter_by(matricula=matricula).first()


def salva_mudancas(data):
    db.session.add(data)
    db.session.commit()
