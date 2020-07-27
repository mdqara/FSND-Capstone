from flask import Flask
from models import setup
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
db = setup(app)

from application import routes

