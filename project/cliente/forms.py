

from django import forms
from core.models import Pais, Cliente  # Ajusta la importación según tu estructura

class PaisForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = ['nombre']
       
       
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'nacimiento', 'pais_origen']


from django import forms

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar')
