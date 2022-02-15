from app.main import db
from app.main.model.lider import Lider


def salva_novo_lider(data):
    lider = Lider.query.filter_by(matricula_lider=data['matricula_lider']).first()

    if not lider:
        lider = Lider(
            matricula_lider=data['matricula_lider']
        )

        salva_mudancas(lider)
        response_object = {
            'status': 'success',
            'message': 'Lider cadastrado com sucesso.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Lider já cadastrado.',
        }
        return response_object, 409


def get_all_lideres():
    return Lider.query.all()


def get_lider(id_lider):
    return Lider.query.filter_by(id_lider=id_lider).first()


def salva_mudancas(data):
    db.session.add(data)
    db.session.commit()
