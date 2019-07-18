from src.app import groceries_list
from src.api.restplus import api
import flask_restplus as swagger

ns = api.namespace('groceries', description='Groceries operations.')

groceries_fields = {'name': swagger.fields.String(required=True, description='The product name (the unique identifier).'),
                    'quantity': swagger.fields.Integer(required=True, description='How many of this product should be bought.')}
groceries_model = api.model('Groceries', groceries_fields)


@ns.route('/')
class GroceriesAPI(swagger.Resource):

    @ns.expect(groceries_model, validate=True)  # for formatting input
    @ns.marshal_with(groceries_model)  # for formatting output
    def post(self):
        """Add products to the groceries list.
        """
        return groceries_list.add(**api.payload), 200

    def get(self):
        """Returns groceries list.
        """
        return groceries_list.get_list()

    @ns.expect(groceries_model, validate=True)
    @ns.marshal_with(groceries_model)
    def delete(self):
        """Deletes a groceries from list.
        """
        return groceries_list.remove(**api.payload)