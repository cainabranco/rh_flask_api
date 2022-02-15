from flask_restx import Resource
from flask import request
from ..util.dto import ColaboradorDto
from ..service.colaborador_service import salva_novo_colaborador, get_colaborador, get_all_colaboradores

api = ColaboradorDto.api
_colaborador = ColaboradorDto.colaborador


@api.route('/')
class ColaboradorList(Resource):
    @api.doc('lista_de_colaboradores_registrados')
    @api.marshal_list_with(_colaborador, envelope='data')
    def get(self):
        """ Lista todos os colaboradores cadastrados """
        return get_all_colaboradores()

    @api.response(201, 'Colaborador cadastrado com sucesso')
    @api.doc('Cria novo colaborador')
    @api.expect(_colaborador, validate=True)
    def post(self):
        """" Cadastra novo colaborador """
        data = request.json
        return salva_novo_colaborador(data=data)


@api.route('/<matricula>')
@api.param('matricula', 'A matricula do colaborador')
@api.response(404, 'Colaborador não encontrado')
class Colaborador(Resource):
    @api.doc('Retorna um colaborador')
    @api.marshal_with(_colaborador)
    def get(self, matricula):
        """ Retorna os dados do colaborador dada uma matricula"""
        colaborador = get_colaborador(matricula=matricula)
        if not colaborador:
            api.abort(404)
        else:
            return colaborador
