from flask_restx import Api
from flask import Blueprint
from .main.controller.colaborador_controller import api as colaborador_ns
from .main.controller.cargo_controller import api as cargo_ns
from .main.controller.lider_controller import api as lider_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='API DE GENTE E GESTÃO COM FASK-RESTX',
          version='1.0')

api.add_namespace(colaborador_ns, path='/colaborador')
api.add_namespace(cargo_ns, path='/cargo')
api.add_namespace(lider_ns, path='/lider')