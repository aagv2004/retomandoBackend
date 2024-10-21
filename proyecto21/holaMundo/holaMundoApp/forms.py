from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO')]

    nombre = forms.CharField(validators=[
        validators.MinLengthValidator(5),
        validators.MaxLengthValidator(20)
    ])
    email = forms.CharField()
    fono = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput())
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
    codigo = forms.IntegerField()

    """ nombre.widget_attrs['class'] = 'form-control'
    email.widget_attrs['class'] = 'form-control'
    fono.widget_attrs['class'] = 'form-control'
    password.widget_attrs['class'] = 'form-control'
    estado.widget_attrs['class'] = 'form-control' """
    
    def clean(self):
        user_clean_data = super().clean()

        inputNombre = user_clean_data['nombre']
        if len(inputNombre) > 20 :
            raise forms.ValidationError('El largo máximo del nombre son 20 caracteres...')
        
        inputEmail = user_clean_data['email']
        if inputEmail.find('@') == -1 :
            raise forms.ValidationError('El correo debe contener @')