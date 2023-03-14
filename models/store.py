from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    # lazy=dynamic means that the items won't be fetched from the db until we tell it to,
    # helps with application speed
    # NOTE: cascade allows us to delete all the items (children) in a store if the store is deleted
    items = db.relationship('ItemModel', back_populates='store', lazy='dynamic', cascade='all, delete')
    tags = db.relationship('TagModel', back_populates='store', lazy='dynamic')