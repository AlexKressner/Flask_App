from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80)) #limit von 80 Zeichen
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        #when the object is initiated the id is not necessary as it is defined as autoincrementing primary key
        self.username = username
        self.password = password

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(username=name).first()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


    def save_to_db(self):
        db.session.add(self) #session collects all the objects to save to the database, self is the object itself
        db.session.commit()
