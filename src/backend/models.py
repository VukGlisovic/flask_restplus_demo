from src.backend.restplus import api
from src.constants import *
import flask_restplus as swagger
import datetime as dt


groceries_info_fields = {QUANTITY: swagger.fields.Integer(required=True,
                                                          min=1,
                                                          description='How many of this product should be bought.',
                                                          example=1),
                         PRICE: swagger.fields.Float(required=True,
                                                     min=0.,
                                                     description='Price of single unit of the product.',
                                                     example=1.5),
                         CATEGORY: swagger.fields.String(required=True,
                                                         enum=CATEGORIES,
                                                         description='The category of the product.',
                                                         example='other'),
                         TIMESTAMP: swagger.fields.DateTime(required=False,
                                                            description='Time of buying.',
                                                            example=dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))}
GroceriesInfoModel = api.model('GroceriesInfo', groceries_info_fields)

groceries_fields = {NAME: swagger.fields.String(required=True, description='The product name (the unique identifier).'),
                    INFO: swagger.fields.Nested(GroceriesInfoModel)}
GroceriesModel = api.model('Groceries', groceries_fields)
