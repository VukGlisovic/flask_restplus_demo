from src.shopping.groceries import GroceriesList
from src.backend.models import *
from flask import request
import flask_restplus as swagger


grocerieslist = GroceriesList(add_defaults=True)

ns = api.namespace('groceries', description='Groceries operations.')


@ns.route('/')
class GroceriesCollection(swagger.Resource):

    @ns.marshal_with(GroceriesModel)
    def get(self):
        """Returns groceries list.
        """
        return grocerieslist.get_list()


@ns.route('/<string:product>')
class GroceriesItem(swagger.Resource):

    @ns.expect(GroceriesInfoModel)  # for formatting input
    @ns.marshal_with(GroceriesModel)  # for formatting output
    def post(self, product):
        """Add products to the groceries list.
        """
        info = request.json
        return grocerieslist.add(product, **info), 200

    @ns.expect(GroceriesInfoModel)
    @ns.marshal_with(GroceriesModel)
    def put(self, product):
        """Update product info on the groceries list.
        """
        info = request.json
        return grocerieslist.update(product, info), 200

    @ns.marshal_with(GroceriesModel)
    def get(self, product):
        """Get one product.
        """
        return grocerieslist.get_product(product)

    @ns.marshal_with(GroceriesModel)
    def delete(self, product):
        """Deletes a groceries from list.
        """
        return grocerieslist.remove(product)
