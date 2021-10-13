from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect, url_for
from utils import isUsernameValid, isEmailValid, isPasswordValid
from forms import Formulario_Login


app = Flask(__name__)
app.secret_key = "Sprint3grupo56"


@app.route('/')
@app.route('/dashboard')
def index():
    return render_template("dashboard.html")
    