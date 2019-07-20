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
        if any([dct.get(name) for dct in self.groceries]):
            raise BadRequest("Product '{}' already exists.".format(name))
        logging.info("Adding %s times '%s' to the groceries list.", quantity, name)
        new_item = {NAME: name, INFO: {QUANTITY: quantity}}
        self.groceries.append(new_item)
        return new_item

    def remove(self, name, quantity):
        logging.info("Removing %s times '%s' from the groceries list.", quantity, name)
        if not self.groceries.get(name):
            raise BadRequest("Product '{}' is not in the shopping list.".format(name))
        product = self.groceries[name]
        resulting_quantity = product[QUANTITY] - quantity
        if resulting_quantity < 0:
            raise BadRequest("Cannot remove this quantity; removing this amount results in a negative amount of '{}' on the list.".format(
                name
            ))
        elif resulting_quantity == 0:
            self.groceries.pop(name)
        else:
            self.groceries[name][QUANTITY] -= quantity
        return {NAME: name, QUANTITY: resulting_quantity}

    def get_list(self):
        logging.info("Listing all groceries.")
        return self.groceries

    def get_product(self, product):
        logging.info("Getting product '{}'.".format(product))
        product_list = [dct for dct in self.groceries if dct[NAME] == product]
        if not any(product_list):
            raise NotFound("No such product on shopping list: '{}'.".format(product))
        return product_list[0]
