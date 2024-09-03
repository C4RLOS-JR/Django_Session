from django import forms

class Cliente(forms.Form):
  nome = forms.CharField(max_length=30, required=False)
  idade = forms.IntegerField(required=False)