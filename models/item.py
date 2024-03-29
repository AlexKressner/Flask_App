from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #make sure that foreign key is used to establish connection between the two tables
    store = db.relationship('StoreModel') #finds the store matching the store_id and returns that store

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #returns an item model object

    def save_to_db(self):
        db.session.add(self) #session collects all the objects to save to the database, self is the object itself
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
