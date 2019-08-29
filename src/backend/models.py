from src.backend.restplus import api
import flask_restplus as swagger
import datetime as dt


groceries_info_fields = {'quantity': swagger.fields.Integer(required=True,
                                                            min=1,
                                                            description='How many of this product should be bought.',
                                                            example=1),
                         'price': swagger.fields.Float(required=True,
                                                       min=0.,
                                                       description='Price of single unit of the product.',
                                                       example=1.5),
                         'timestamp': swagger.fields.DateTime(required=False,
                                                              default=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                                                              description='Time of buying.',
                                                              example=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))}
GroceriesInfoModel = api.model('GroceriesInfo', groceries_info_fields)

groceries_fields = {'name': swagger.fields.String(required=True, description='The product name (the unique identifier).'),
                    'info': swagger.fields.Nested(GroceriesInfoModel)}
GroceriesModel = api.model('Groceries', groceries_fields)
