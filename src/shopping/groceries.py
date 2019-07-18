import logging
from werkzeug.exceptions import BadRequest


NAME = 'name'
QUANTITY = 'quantity'


class GroceriesList(object):

    def __init__(self, add_defaults=True):
        logging.info("Setting up groceries list.")
        self.groceries = {}
        if add_defaults:
            self.add('milk', 2)
            self.add('peanut butter', 5)

    def add(self, name, quantity):
        self.check_valid_quantity(quantity)
        if self.groceries.get(name):
            logging.info("Product '%s' is already on the list. Updating it now.")
            self.groceries[name][QUANTITY] += quantity
            return {NAME: name, QUANTITY: self.groceries[name][QUANTITY]}
        logging.info("Adding %s times '%s' to the groceries list.", quantity, name)
        self.groceries[name] = {QUANTITY: quantity}
        return {NAME: name, QUANTITY: quantity}

    def remove(self, name, quantity):
        self.check_valid_quantity(quantity)
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

    @classmethod
    def check_valid_quantity(cls, quantity):
        if quantity <= 0:
            raise BadRequest("Not allowed to add a quantity smaller or equal than zero.")
