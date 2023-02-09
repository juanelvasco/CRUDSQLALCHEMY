from flask import Flask
from routes.vehiculos import vehiculos
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)
app.secret_key = 'clave'
# dialect://username:password@host:port/database
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)


app.register_blueprint(vehiculos)
