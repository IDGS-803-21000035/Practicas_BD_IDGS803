from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, BooleanField
#esta clase sirve para las validaciones 
from wtforms import validators

class EmpleadoForms(Form):
    id = IntegerField('id')
    nombre = StringField('nombre',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa nombre valido')
    ])
    sueldo = IntegerField('sueldo',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un sueldo valido')
    ])
    telefono = StringField('telefono',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un telefono valido')
    ])
    direccion = StringField('direccion',[
        validators.DataRequired(message = 'El campo es requerido')
    ])
    correo = EmailField('correo',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.Email(message = 'Ingresa un correo valido')
    ])

class PizzaForms(Form):
    id = IntegerField('id')
    nombre = StringField('nombre',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa nombre valido')
    ])
    telefono = StringField('telefono',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa un telefono valido')
    ])
    direccion = StringField('direccion',[
        validators.DataRequired(message = 'El campo es requerido')
    ])

    tamanios = [('Chica', 'Chica $40'), ('Mediana', 'Mediana $80'), ('Grande', 'Grande $120')]
    tamanio = RadioField('Tamaño: ', choices=tamanios)

    opciones = [('Jamon', 'Jamón $10'), ('Piña', 'Piña $10'), ('Champiñones', 'Champiñones $10')]
    ingredientes = RadioField('Ingredientes: ', choices=opciones)

    numPizas = IntegerField('numPizas')
