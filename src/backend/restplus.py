import logging
from flask_restplus import Api
from src import settings
from jsonschema import FormatChecker


api = Api(version='1.0',
          title='Groceries API',
          description='For creating a shopping list for the groceries.',
          format_checker=FormatChecker(formats=['date-time']))  # add the jsonschema formatcheckers here


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    logging.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
