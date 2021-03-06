import os
import unittest
from flask_migrate import Migrate
from app.main import create_app, db
from app import blueprint
from app.main.model import colaborador, cargo, lider


app = create_app(os.getenv('RH_FLASK_ENV') or 'dev')
app.register_blueprint(blueprint=blueprint)
app.app_context().push()

migrate = Migrate(app, db)


def run():
    app.run()


def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


""" Verificar motivo do comando 'python manage.py test' não executar a função 'test' """
if __name__ == '__main__':
    run()
