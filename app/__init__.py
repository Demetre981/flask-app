from flask import Flask

app = Flask(__name__)
app.secret_key ="eWPrsDUYC8Qcx8ESFLa3qTgN"

from app import routes