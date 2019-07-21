from src.backend.models import *
from src.shopping.groceries import *
from flask import request
import flask_restplus as swagger


ns = api.namespace('groceries', description='Groceries operations.')


@ns.route('/')
class GroceriesCollection(swagger.Resource):

    @ns.marshal_with(ProductModel)
    def get(self):
        """Returns groceries list.
        """
        return get_full_list()


@ns.route('/<string:product>')
class GroceriesItem(swagger.Resource):

    @ns.expect(ProductInfoModel)  # for formatting input
    @ns.marshal_with(ProductModel)  # for formatting output
    def post(self, product):
        """Add products to the groceries list.
        """
        info = request.json
        return add_product(product, **info), 200

    @ns.expect(ProductInfoModel)
    @ns.marshal_with(ProductModel)
    def put(self, product):
        """Update product info of a product.
        """
        info = request.json
        return update_product(product, **info), 200

    @ns.marshal_with(ProductModel)
    def get(self, product):
        """Get one product.
        """
        return get_product(product)

    @ns.marshal_with(ProductModel)
    def delete(self, product):
        """Deletes a groceries from list.
        """
        return remove_product(product)
