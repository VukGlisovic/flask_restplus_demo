from src.database import db
import datetime as dt


class Product(db.Model):

    name = db.Column(db.String(80), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80))
    price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=dt.datetime.utcnow)

    def __init__(self, name, quantity, category, price, timestamp=None):
        self.name = name
        self.quantity = quantity
        self.category = category
        self.price = price
        if timestamp is None:
            timestamp = dt.datetime.utcnow()
        self.timestamp = timestamp

    def __repr__(self):
        return '<Product(%r)>' % self.name
