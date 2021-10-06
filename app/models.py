from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    price_cents = db.Column(db.Integer)
    delivery_available = db.Column(db.Boolean)