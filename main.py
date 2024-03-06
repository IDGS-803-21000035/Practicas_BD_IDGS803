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

@app.route("/pizza", methods=["GET", "POST"])
def piza():
    pizz_form = forms.PizzaForms(request.form)
    return render_template("pizzeria.html", form = pizz_form)

@app.route("/cliente", methods=["GET", "POST"])
def venta():
    pizz_form = forms.PizzaForms(request.form)
    if request.method == "POST":
        pass  
        
        return render_template("pizzeria.html", form = pizz_form)
            


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

@app.route('/eliminar', methods=["GET","POST"])
def eliminar():
    empl_form = forms.EmpleadoForms(request.form)
    if request.method=="GET":
        id = request.args.get('id')
        emp1 = db.session.query(Empleados).filter(Empleados.id==id).first()
        empl_form.id.data=request.args.get('id')
        empl_form.nombre.data=emp1.nombre
        empl_form.correo.data=emp1.correo
        empl_form.telefono.data=emp1.telefono
        empl_form.direccion.data=emp1.direccion
        empl_form.sueldo.data=emp1.sueldo
    if request.method=="POST":
        id = empl_form.id.data
        emp = Empleados.query.get(id)
        db.session.delete(emp)
        db.session.commit()
        return redirect('ABC')
    return render_template('eliminar.html', form= empl_form)

@app.route('/modificar', methods=["GET","POST"])
def modificar():
    empl_form = forms.EmpleadoForms(request.form)
    if request.method=="GET":
        id = request.args.get('id')
        emp1 = db.session.query(Empleados).filter(Empleados.id==id).first()
        empl_form.id.data=request.args.get('id')
        empl_form.nombre.data=emp1.nombre
        empl_form.correo.data=emp1.correo
        empl_form.telefono.data=emp1.telefono
        empl_form.direccion.data=emp1.direccion
        empl_form.sueldo.data=emp1.sueldo
    if request.method=="POST":
        id = empl_form.id.data
        emp = db.session.query(Empleados).filter(Empleados.id==id).first()
        emp.nombre = empl_form.nombre.data
        emp.correo = empl_form.correo.data
        emp.telefono = empl_form.telefono.data
        emp.direccion = empl_form.direccion.data
        emp.sueldo = empl_form.sueldo.data
        db.session.add(emp)
        db.session.commit()
        return redirect('ABC')
    return render_template('modificar.html', form = empl_form)

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