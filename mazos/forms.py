from django import forms
from .models import Arena, Tropa, Ejercito

class ArenaForm(forms.ModelForm):
    #todos los campos de Arena
    class Meta:
        model = Arena
        fields = ('nombre', 'nivel', 'tropas')

#Redefinimos que control (widget) vamos a mostrar para ingresar las tropas.

#Cuando el modelo es Many To Many, por defecto se usa un lisbotx multiseleccionable.

def __init__ (self, *args, **kwargs):
        super(ArenaForm, self).__init__(*args, **kwargs)

#En este caso vamos a usar el widget checkbox multiseleccionable.
        self.fields["tropas"].widget = forms.widgets.CheckboxSelectMultiple()
#Podemos usar un texto de ayuda en el widget
        self.fields["tropas"].help_text = "Ingrese las tropas que pertenecen a esta arena"
#En este caso le indicamos que nos muestre todas las tropas, pero aquí podríamos filtrar datos si fuera necesario
        self.fields["tropas"].queryset = Tropa.objects.all()
