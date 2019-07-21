import logging
from werkzeug.exceptions import BadRequest, NotFound
from sqlalchemy import exc
from src.constants import *
from src.database import db
import src.database.models as db_models


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
    product = db_models.Product(name, quantity, category, price)
    check_product_exists(name, should_exist=False)
    db.session.add(product)
    db.session.commit()
    return product.to_api_model_dict()


@catch_integrity_error
def get_product(name):
    product = db.session.execute("SELECT * FROM product WHERE name='{}' ORDER BY timestamp DESC".format(name)).first()
    if product is None:
        raise BadRequest("No such product '{}'.".format(name))
    return db_models.Product(**dict(product)).to_api_model_dict()


def get_full_list():
    product_list = db.session.execute("SELECT * FROM product WHERE timestamp IN "
                                      "(SELECT MAX(timestamp) AS max_ts FROM product GROUP BY name ORDER BY timestamp DESC)").fetchall()
    return [db_models.Product(**dict(p)).to_api_model_dict() for p in product_list]


def check_product_exists(name, should_exist=True):
    """
    Args:
        name (str):
        should_exist (bool):

    Returns:
        rowProxy
    """
    product = db_models.Product.query.filter_by(name=name).first()
    if should_exist:
        if product is None:
            raise BadRequest("Product '{}' doesn't exist.".format(name))
    else:
        if product is not None:
            raise BadRequest("Product '{}' already exists.".format(name))
    return product


class GroceriesList(object):

    def __init__(self, add_defaults=True):
        logging.info("Setting up groceries list.")
        self.groceries = []
        if add_defaults:
            self.add('milk', 2)
            self.add('peanut butter', 5)

    def add(self, name, quantity, **kwargs):
        """
        Args:
            name (str):
            quantity (int):
            **kwargs:

        Returns:
            dict
        """
        self.check_product_exists(name, should_exist=False)
        logging.info("Adding %s times '%s' to the groceries list.", quantity, name)
        new_item = {NAME: name, INFO: {QUANTITY: quantity}}
        self.groceries.append(new_item)
        return new_item

    def update(self, name, info):
        """
        Args:
            name (str):
            info (dict):

        Returns:
            dict
        """
        product_dict = self.check_product_exists(name, should_exist=True)
        # changes original object by reference
        product_dict[INFO] = info
        return product_dict

    def remove(self, name):
        """
        Args:
            name (str):

        Returns:
            dict
        """
        products_dict = self.check_product_exists(name, should_exist=True)
        self.groceries.remove(products_dict)
        return products_dict

    def get_list(self):
        """
        Returns:
            list[dict]
        """
        logging.info("Listing all groceries.")
        return self.groceries

    def get_product(self, product):
        """
        Args:
            product (str):

        Returns:
            dict
        """
        logging.info("Getting product '{}'.".format(product))
        product_dict = self.check_product_exists(product, should_exist=True)
        return product_dict

    def check_product_exists(self, name, should_exist=True):
        """
        Args:
            name (str):
            should_exist (bool):

        Returns:
            Union[dict, None]
        """
        product_list = [dct for dct in self.groceries if dct[NAME] == name]
        if should_exist:
            if not any(product_list):
                raise NotFound("No such product on shopping list: '{}'.".format(name))
            if len(product_list) > 1:
                logging.warning("More than one product with name '%s' found", name)
            return product_list[0]
        else:
            if any(product_list):
                raise BadRequest("Product '{}' already exists.".format(name))
