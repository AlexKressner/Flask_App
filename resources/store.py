from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json() #default is 200
        return {'message' : f'Store with name {name} does not exist!'}, 404


    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'messsage' : f"The store with name {name} already exists!"}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message' : 'An error occured!'}, 500 #internal server error

        return store.json(), 201


    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': f'Store {name} was deleted!'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
