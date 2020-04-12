from django import forms

class StacionIdForm(forms.Form):
    stacion_id = forms.CharField(label='Enter the ID')