from src import app
from src.api.restplus import api
from src.api.models import GroceriesModel
import flask_restplus as swagger


ns = api.namespace('groceries', description='Groceries operations.')


@ns.route('/')
class GroceriesAPI(swagger.Resource):

    @ns.expect(GroceriesModel, validate=True)  # for formatting input
    @ns.marshal_with(GroceriesModel)  # for formatting output
    def post(self):
        """Add products to the groceries list.
        """
        return app.grocerieslist.add(**api.payload), 200

    def get(self):
        """Returns groceries list.
        """
        return app.grocerieslist.get_list()

    @ns.expect(GroceriesModel, validate=True)
    @ns.marshal_with(GroceriesModel)
    def delete(self):
        """Deletes a groceries from list.
        """
        return app.grocerieslist.remove(**api.payload)