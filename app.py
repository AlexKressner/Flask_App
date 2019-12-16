import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db') #first parameter reads the environment variable, default is 'sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False #change extension behavior and use SQLAlchemy internal modification tracker
app.secret_key = 'Alex'
api = Api(app)


jwt = JWT(app, authenticate, identity) #/auth endpoint

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':
    @app.before_first_request
    def create_tables():
        db.create_all()
        
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
