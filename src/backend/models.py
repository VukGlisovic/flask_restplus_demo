from src.backend.restplus import api
import flask_restplus as swagger


product_info_fields = {'quantity': swagger.fields.Integer(required=True, min=1, description='How many of this product should be bought.'),
                       'category': swagger.fields.String(min_length=1, enum=['vegetable', 'fruit', 'meat', 'fish', 'dairy', 'other'],
                                                         description='The category of the product.'),
                       'price': swagger.fields.Float(min=0., description='How much does the product cost.')}
ProductInfoModel = api.model('ProductInfo', product_info_fields)

product_fields = {'name': swagger.fields.String(required=True, description='The product name (the unique identifier).'),
                  'info': swagger.fields.Nested(ProductInfoModel)}
ProductModel = api.model('Groceries', product_fields)
