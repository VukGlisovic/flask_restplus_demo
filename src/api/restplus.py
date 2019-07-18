import logging
from flask_restplus import Api
from src import settings


api = Api(version='1.0',
          title='Groceries API',
          description='For creating a shopping list for the groceries.')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    logging.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
