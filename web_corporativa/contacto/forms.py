from django import forms
from django.forms.widgets import TextInput

class FormularioContacto(forms.Form):
    name=forms.CharField(
            label="Nombre",
            required=True,
            min_length=3,
            max_length=100,
            widget=forms.TextInput(
                attrs={
                    'placeholder':"Escribe tu nombre",
                    'class':'form-control'
                }
            )
        )

    email=forms.EmailField(
            label="Email",
            required=True,
            widget=forms.EmailInput(
                attrs={
                    'placeholder':"Escribe tu email",
                    'class':'form-control'
                }
            )
        )
    content=forms.CharField(
            label="Contenido",
            required=True,
            widget=forms.Textarea(
                attrs={
                    'placeholder':"Escribe tu mensaje",
                    'class':'form-control',
                    'rows':3
                }
            ) 
        )
    

    #def clean_email(self):
    #    correo=self.cleaned_data['email']
    #    if not correo.endswith('gmail.com'):
    #        raise forms.ValidationError("El correo de contacto debe ser un correo de gmail, es decir tu correo proporcionado deberia tener una terminacion 'gmail.com' ")
    #    return correo
    