from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    description = db.Column(db.String)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), unique=False, nullable=False)
    # SQLAlchemy knows that we're using the stores table (above) from the StoreModel class (below),
    # so it will automatically populate the 'store' variable with a StoreModel object whose id
    # matches that of the foreign key ('stores.id')
    # 'back_populates' means that the StoreModel class will also have an 'items' relationship
    # that allows the StoreModel to see all the items that are associated with it
    store = db.relationship('StoreModel', back_populates='items')
    tags = db.relationship('TagModel', secondary='items_tags', back_populates='items')