from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
#esta clase sirve para las validaciones 
from wtforms import validators

class EmpleadoForms(Form):
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

