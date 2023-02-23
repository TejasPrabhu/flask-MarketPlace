from market import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    items = db.relationship("Item", backref="user", lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(12), unique=True, nullable=False)
    description = db.Column(db.String(1024), unique=True, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
