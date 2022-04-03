from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nome = StringField('Nome', [validators.Length(min=4, max=25)])
    usuario = StringField('usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    senha = PasswordField('Digite sua senha', [
        validators.DataRequired(),
        validators.EqualTo('Confirmar sua senha', message='As senhas devem ser iguais')
    ])
    confirmacao = PasswordField('Confirmar sua senha')