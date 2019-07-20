from src.backend.restplus import api
import flask_restplus as swagger


groceries_info_fields = {'quantity': swagger.fields.Integer(required=True, min=1, description='How many of this product should be bought.')}
GroceriesInfoModel = api.model('GroceriesInfo', groceries_info_fields)

groceries_fields = {'name': swagger.fields.String(required=True, description='The product name (the unique identifier).'),
                    'info': swagger.fields.Nested(GroceriesInfoModel)}
GroceriesModel = api.model('Groceries', groceries_fields)
