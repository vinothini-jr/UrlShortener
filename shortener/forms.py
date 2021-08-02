from django import forms
from.models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model=Data
        fields=['link']


        widgets = {
            'link':forms.TextInput(attrs={'class':'form-control','placeholder':'paste the link'}),
        }

