from cartaoApp.models import Validar
from django import forms
class ValidarForm(forms.ModelForm):
    class Meta:
        model =Validar
        fields= '__all__'
