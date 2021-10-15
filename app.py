from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask import redirect, url_for
from utils import isUsernameValid, isEmailValid, isPasswordValid
from forms import Formulario_Login
from dshbd import headings #esto se usa para los datos de la tabla del dashboard
from dshbd import data #esto se usa para los datos de la tabla del dashboard


app = Flask(__name__)
app.secret_key = "Sprint3grupo56"


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", headings=headings, data=data)
    

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/cliente')
def cliente():
    return render_template("cliente.html")

@app.route('/citas', methods=['GET', 'POST'])
def citas():
    return render_template("citas.html")