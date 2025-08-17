from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config import Config
from flask_socketio import SocketIO


mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins="*", logger=True, engineio_logger=True) 

def create_app():
    """Flask application factory"""
    app = Flask(__name__)
    app.config.from_object(Config)


    mongo.init_app(app)
    if mongo.db is None:
        print("MongoDB connection failed!")

    bcrypt.init_app(app)
    CORS(app)
    jwt.init_app(app)
    socketio.init_app(app)

    return app
