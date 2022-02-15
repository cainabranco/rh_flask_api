from flask_restx import Resource
from flask import request
from ..util.dto import LiderDto
from ..service.lider_service import salva_novo_lider, get_lider, get_all_lideres

api = LiderDto.api
_lider = LiderDto.lider


@api.route('/')
class LiderList(Resource):
    @api.doc('lista_de_lideres_registrados')
    @api.marshal_list_with(_lider, envelope='data')
    def get(self):
        """ Lista todos os lideres cadastrados """
        return get_all_lideres()

    @api.response(201, 'Lider cadastrado com sucesso')
    @api.doc('Cria novo lider')
    @api.expect(_lider, validate=True)
    def post(self):
        """" Cadastra novo colaborador """
        data = request.json
        return salva_novo_lider(data=data)


@api.route('/<id_lider>')
@api.param('id_lider', 'O identificador único do lider')
@api.response(404, 'Lider não encontrado')
class Lider(Resource):
    @api.doc('Retorna um lider')
    @api.marshal_with(_lider)
    def get(self, id_lider):
        """ Retorna os dados do lider dado seu identificador (id_lider)"""
        lider = get_lider(id_lider=id_lider)
        if not lider:
            api.abort(404)
        else:
            return lider
