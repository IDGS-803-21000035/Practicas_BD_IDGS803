from flask_sqlalchemy import SQLAlchemy

import datetime

#instancia
db = SQLAlchemy()

#clase = tabla
#se crea in id siempre
class Empleados(db.Model):
    __tablename__ = "empleados"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    correo = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    sueldo = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)


class Clientes(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(100))
    telefono = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    pedidos = db.relationship('Pedidos', backref='cliente', lazy=True)

class Pizzas(db.Model):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    tamanio = db.Column(db.String(100))
    ingredientes = db.Column(db.String(100))
    numPizzas = db.Column(db.Integer)

class Pedidos(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    fecha = db.Column(db.DateTime, default=datetime.datetime.now)
    detalles = db.relationship('DetallePedido', backref='pedido', lazy=True)

class DetallePedido(db.Model):
    __tablename__ = "detalle_pedido"
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    subtotal = db.Column(db.Float)
