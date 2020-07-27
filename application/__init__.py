from flask import Flask

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


from application import routes

