from flask_restx import Namespace, fields


class ColaboradorDto:
    api = Namespace('colaborador', description='Operações relacionadas a Colaboradores')
    colaborador = api.model('colaborador',
                            {
                                'nome': fields.String(required=True),
                                'sobrenome': fields.String(required=True),
                                'id_cargo': fields.Integer(required=True),
                                'id_lider': fields.Integer(),
                                'email': fields.String(required=True),
                                'senha': fields.String(required=True),
                                'salario': fields.Float(required=True)
                            })


class CargoDto:
    api = Namespace('cargo', description='Operações relacionadas a Cargos')
    cargo = api.model('cargo',
                      {
                          'cargo': fields.String(required=True),
                          'descricao': fields.String()
                      })


class LiderDto:
    api = Namespace('lider', description='Operações relacionadas a Lideres')
    cargo = api.model('lider',
                      {
                          'matricula_lider': fields.Integer(required=True)
                      })
