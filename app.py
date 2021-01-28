from flask import Flask, render_template
from flask_restful import Api
import requests

import os

# intern package
from db import db
from utils import initialize_models
from config import database_name
from resources.Summarizer import Summarizer, SummarizerList
from resources.BartModel import BartModel


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", f"sqlite:///{database_name}")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
api = Api(app)

api.add_resource(Summarizer, "/text/<int:id_>")
api.add_resource(BartModel, "/summary/<int:id_>")
api.add_resource(SummarizerList, "/texts")


@app.before_first_request
def create_tables():
    db.create_all()

# initialize the ML models
#model, tokenizer = initialize_models()


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
