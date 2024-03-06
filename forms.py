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

    tamanios = [('0', 'Chica'), ('1', 'Mediana'), ('2', 'Grande')]
    tamanio = RadioField('Ingredientes: ', choices=tamanios)

    

    opciones = [('0', 'Jamón $10'), ('1', 'Piña $10'), ('2', 'Champiñones $10')]
    intredientes = RadioField('Ingredientes: ', choices=opciones)


    numPizas = IntegerField('numPizas')
