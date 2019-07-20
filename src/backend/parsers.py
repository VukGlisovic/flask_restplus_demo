from flask_restplus import reqparse


groceries_arguments = reqparse.RequestParser()
groceries_arguments.add_argument('quantity', type=int, required=True)
