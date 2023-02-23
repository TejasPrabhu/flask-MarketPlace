import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# DB_CONNECTION_STRING = (
#     os.environ["DB_CONNECTION_STRING"] + "&ssl_ca=/path/to/ca.pem&ssl_verify_cert=true"
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = DB_CONNECTION_STRING
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"

db = SQLAlchemy(app)

from market import routes
