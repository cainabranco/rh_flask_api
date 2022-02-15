from app.main import db
from app.main.model.cargo import Cargo


def salva_novo_cargo(data):
    cargo = Cargo.query.filter_by(cargo=data['cargo']).first()

    if not cargo:
        cargo = Cargo(
            cargo=data['cargo'],
            descricao=data['descricao'],
        )

        salva_mudancas(cargo)
        response_object = {
            'status': 'success',
            'message': 'Cargo cadastrado com sucesso.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Cargo já cadastrado.',
        }
        return response_object, 409


def get_all_cargos():
    return Cargo.query.all()


def get_cargo(id_cargo):
    return Cargo.query.filter_by(id_cargo=id_cargo).first()


def salva_mudancas(data):
    db.session.add(data)
    db.session.commit()
