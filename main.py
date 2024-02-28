from flask import Flask, render_template, request, flash, Response
#proceso de seguridad
from flask_wtf.csrf import CSRFProtect
from flask import redirect
#variable global
from flask import g

from config import DevelopmentConfig

import forms
#importación de las tablas
from models import db, Empleados

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route("/index", methods=["GET", "POST"])
def index():
    empl_form = forms.EmpleadoForms(request.form)
    if request.method == 'POST':
        #instancia de clase
        em = Empleados(nombre=empl_form.nombre.data, 
                        correo = empl_form.correo.data, 
                        telefono = empl_form.telefono.data,
                        direccion = empl_form.direccion.data,
                        sueldo = empl_form.sueldo.data)

        #usar orm, con add inserto parametros
        db.session.add(em)
        #guardar ddatos
        db.session.commit()
    
    return render_template("index.html", form = empl_form)

@app.route("/ABC", methods = ["GET","POST"])
def ABC_Completo():
    empl_form = forms.EmpleadoForms(request.form)
    empleado = Empleados.query.all()
    return render_template("ABC_Completo.html", empleados = empleado)


if __name__== "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()