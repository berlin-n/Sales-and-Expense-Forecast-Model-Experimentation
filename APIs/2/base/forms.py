from django import forms

class PredictionForm(forms.Form):
    month1 = forms.FloatField()
    month2 = forms.FloatField()
    month3 = forms.FloatField()
    month4 = forms.FloatField()