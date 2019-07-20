from src import app
from src.api.restplus import api
from src.api.models import GroceriesModel
from src.api.parsers import groceries_arguments
from flask import request
import flask_restplus as swagger


ns = api.namespace('groceries', description='Groceries operations.')


@ns.route('/')
class GroceriesCollection(swagger.Resource):

    @ns.expect(GroceriesModel, validate=True)  # for formatting input
    @ns.marshal_with(GroceriesModel)  # for formatting output
    def post(self):
        """Add products to the groceries list.
        """
        return app.grocerieslist.add(**api.payload), 200

    @ns.marshal_list_with(GroceriesModel)
    def get(self):
        """Returns groceries list.
        """
        return app.grocerieslist.get_list()


@ns.route('/<string:product>')
class GroceriesItem(swagger.Resource):

    @ns.expect(groceries_arguments)  # for formatting input
    @ns.marshal_with(GroceriesModel)  # for formatting output
    def post(self, product):
        """Add products to the groceries list. Can also add to existing products.
        """
        args = groceries_arguments.parse_args(request)
        quantity = args.get('quantity')
        return app.grocerieslist.add(product, quantity), 200

    @ns.marshal_with(GroceriesModel)
    def get(self, product):
        """Get one product.
        """
        return app.grocerieslist.get_product(product)

    @ns.expect(GroceriesModel, validate=True)
    @ns.marshal_with(GroceriesModel)
    def delete(self, product):
        """Deletes a groceries from list.
        """
        return app.grocerieslist.remove(**api.payload)
