from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    items = db.relationship('ItemModel', lazy='dynamic')
    #if lazy is not used for each item belonging to the (new) store an item object is created which can take substantial 
    #memory. if lazy is used items becomes a query builder which is called on demand

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #returns an item model object

    def save_to_db(self):
        db.session.add(self) #session collects all the objects to save to the database, self is the object itself
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
