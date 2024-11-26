from django import forms
from .models import Datos
from .models import ResetaP

class DatosForm(forms.ModelForm):

    class Meta:
        model = Datos
        fields = '__all__'

class ResetaPForm(forms.ModelForm):

    class Meta:
        model = ResetaP
        fields = '__all__'

        widgets = {
            "fecha_Consumo": forms.SelectDateWidget()
        }