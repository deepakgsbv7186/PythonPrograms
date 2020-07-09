from django import forms

class inrTousd(forms.Form):
    usd = forms.CharField()
    inr = forms.CharField(disabled=True)
    
