from werkzeug.exceptions import BadRequest, NotFound
from sqlalchemy import exc
from src.database import db
import src.database.models as db_models
from src.constants import *


def catch_integrity_error(fnc):
    def wrapper(*args, **kwargs):
        try:
            result = fnc(*args, **kwargs)
        except exc.IntegrityError as e:
            raise BadRequest(e.args[0])
        return result
    return wrapper


@catch_integrity_error
def add_product(name, quantity, category, price, *args, **kwargs):
    check_product_exists(name, should_exist=False)
    product = db_models.Product(name, quantity, category, price)
    db.session.add(product)
    db.session.commit()
    return product.to_api_model_dict()


@catch_integrity_error
def get_product(name):
    product = check_product_exists(name, should_exist=True)
    return product.to_api_model_dict()


def get_full_list():
    product_list = db.session.execute("SELECT * FROM product WHERE quantity > 0 AND timestamp IN "
                                      "(SELECT MAX(timestamp) AS max_ts FROM product GROUP BY name ORDER BY timestamp DESC)").fetchall()
    return [db_models.Product(**dict(p)).to_api_model_dict() for p in product_list]


@catch_integrity_error
def update_product(name, quantity, category, price, *args, **kwargs):
    check_product_exists(name, should_exist=True)
    product = db_models.Product(name, quantity, category, price)
    db.session.add(product)
    db.session.commit()
    return product.to_api_model_dict()


@catch_integrity_error
def remove_product(name):
    product = check_product_exists(name, should_exist=True)
    product_dict = product.__dict__
    quantity = 0
    category = product_dict.pop(CATEGORY)
    price = product_dict.pop(PRICE)
    product = db_models.Product(name, quantity, category, price)
    db.session.add(product)
    db.session.commit()
    return product.to_api_model_dict()


def check_product_exists(name, should_exist=True):
    """
    Args:
        name (str):
        should_exist (bool):

    Returns:
        Product
    """
    product = db.session.execute("SELECT * FROM product WHERE name='{}' ORDER BY timestamp DESC".format(name)).first()
    product = db_models.Product(**dict(product)) if product is not None else None
    if should_exist:
        if product is None or getattr(product, QUANTITY) == 0:
            raise NotFound("Product '{}' doesn't exist.".format(name))
    else:
        if product is not None and getattr(product, QUANTITY) > 0:
            raise BadRequest("Product '{}' already exists.".format(name))
    return product
