from application import routes
from flask import Flask
from models import setup_db
from flask_cors import CORS
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
database_path = os.environ.get('DATABASE_URL')
setup_db(app, database_path)
