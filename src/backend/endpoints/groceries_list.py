from src import app
from src.backend.restplus import api
from src.backend.models import *
from src.backend.parsers import groceries_arguments
from src.constants import *
from flask import request
import flask_restplus as swagger


ns = api.namespace('groceries', description='Groceries operations.')


@ns.route('/')
class GroceriesCollection(swagger.Resource):

    @ns.marshal_with(GroceriesModel)
    def get(self):
        """Returns groceries list.
        """
        return app.grocerieslist.get_list()


@ns.route('/<string:product>')
class GroceriesItem(swagger.Resource):

    @ns.expect(GroceriesInfoModel)  # for formatting input
    @ns.marshal_with(GroceriesModel)  # for formatting output
    def post(self, product):
        """Add products to the groceries list.
        """
        info = request.json
        return app.grocerieslist.add(product, **info), 200

    @ns.expect(GroceriesInfoModel)
    @ns.marshal_with(GroceriesModel)
    def put(self, product):
        """Update product info on the groceries list.
        """
        info = request.json
        return app.grocerieslist.update(product, info), 200

    @ns.marshal_with(GroceriesModel)
    def get(self, product):
        """Get one product.
        """
        return app.grocerieslist.get_product(product)

    @ns.marshal_with(GroceriesModel)
    def delete(self, product):
        """Deletes a groceries from list.
        """
        return app.grocerieslist.remove(product)
