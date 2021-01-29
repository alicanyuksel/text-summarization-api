from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS, cross_origin
import requests

import os

# intern package
from config import model_name, tokenizer_name
from resources.BartModel import BartModel, initialize_model

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

api.add_resource(BartModel, "/summary")

# initialize the ML models to get the best inference time on CPU...
initialize_model()

if __name__ == "__main__":
    app.run(port=5000, debug=True)
