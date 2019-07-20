import logging
from werkzeug.exceptions import BadRequest, NotFound
from src.constants import *


class GroceriesList(object):

    def __init__(self, add_defaults=True):
        logging.info("Setting up groceries list.")
        self.groceries = []
        if add_defaults:
            self.add('milk', 2)
            self.add('peanut butter', 5)

    def add(self, name, quantity, **kwargs):
        self.check_product_exists(name, should_exist=False)
        logging.info("Adding %s times '%s' to the groceries list.", quantity, name)
        new_item = {NAME: name, INFO: {QUANTITY: quantity}}
        self.groceries.append(new_item)
        return new_item

    def update(self, name, info):
        product_dict = self.check_product_exists(name, should_exist=True)
        # changes original object by reference
        product_dict[INFO] = info
        return product_dict

    def remove(self, name):
        products_dict = self.check_product_exists(name, should_exist=True)
        self.groceries.remove(products_dict)
        return products_dict

    def get_list(self):
        logging.info("Listing all groceries.")
        return self.groceries

    def get_product(self, product):
        logging.info("Getting product '{}'.".format(product))
        product_dict = self.check_product_exists(product, should_exist=True)
        return product_dict

    def check_product_exists(self, name, should_exist=True):
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
