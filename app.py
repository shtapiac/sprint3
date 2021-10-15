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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Formulario_Login(request.form)
    if request.method == 'POST' and form.validate():
        usuario = form.usuario.data
        password = form.password.data 

        error = None

        if not usuario:
            error = "Usuario requerido."
            flash(error)
        if not password:
            error = "ContraseÃ±a requerida."
            flash(error)

        if error is not None:
            return render_template("login.html", form=form)
        else:
            if usuario == "Prueba" and password == "Prueba123":
                #Usuario: Prueba
                #ContraseÃ±a: Prueba123                
                return redirect( 'inicio' )
            elif usuario == "Admin" and password == "Admin123":
                #Usuario: Prueba
                #ContraseÃ±a: Prueba123                
                return redirect( 'dashboard' )     
            else:
                flash('Usuario y contraseÃ±a no son correctos.')
                return render_template("login.html", form=form)  
               
    # GET:  
    return render_template("login.html", form=form)





@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", headings=headings, data=data)
    

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/inicio')
def cliente():
    return render_template("cliente.html")

@app.route('/detalles', methods=['GET', 'POST'])
def detalles():
    return render_template("detalles.html")

@app.route('/citas')
def citas():
    return render_template("citas.html")