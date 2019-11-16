from app import app
from db import db

db.init_app(app)

#creates the databasae as defined by the URI and all the tables on the fly before the app runs
@app.before_first_request
def create_tables():
    db.create_all()
