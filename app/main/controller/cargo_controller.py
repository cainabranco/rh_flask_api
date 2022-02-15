from flask_restx import Resource
from flask import request
from ..util.dto import CargoDto
from ..service.cargo_service import salva_novo_cargo, get_cargo, get_all_cargos

api = CargoDto.api
_cargo = CargoDto.cargo


@api.route('/')
class CargoList(Resource):
    @api.doc('lista_de_cargos_registrados')
    @api.marshal_list_with(_cargo, envelope='data')
    def get(self):
        """ Lista todos os cargos cadastrados """
        return get_all_cargos()

    @api.response(201, 'Cargo cadastrado com sucesso')
    @api.doc('Cria novo cargo')
    @api.expect(_cargo, validate=True)
    def post(self):
        """" Cadastra novo colaborador """
        data = request.json
        return salva_novo_cargo(data=data)


@api.route('/<id_cargo>')
@api.param('id_cargo', 'O identificador único do cargo')
@api.response(404, 'Cargo não encontrado')
class Cargo(Resource):
    @api.doc('Retorna um cargo')
    @api.marshal_with(_cargo)
    def get(self, id_cargo):
        """ Retorna os dados do cargo dado seu identificador (id_cargo)"""
        cargo = get_cargo(id_cargo=id_cargo)
        if not cargo:
            api.abort(404)
        else:
            return cargo
