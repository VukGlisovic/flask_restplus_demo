from src.api.restplus import api
import flask_restplus as swagger


groceries_fields = {'name': swagger.fields.String(required=True, description='The product name (the unique identifier).'),
                    'quantity': swagger.fields.Integer(required=True, description='How many of this product should be bought.')}
GroceriesModel = api.model('Groceries', groceries_fields)
