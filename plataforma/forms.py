from django import forms
from .models import Livros

class Cliente(forms.Form):
  nome = forms.CharField(max_length=30, required=False)
  idade = forms.IntegerField(required=False)
  data = forms.DateField()
  email = forms.EmailField()

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['nome'].widget.attrs['class'] = 'form-control'
    self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
    
    self.fields['idade'].widget.attrs['class'] = 'form-control'
    self.fields['idade'].widget.attrs['placeholder'] = 'Digite sua idade'
    
    self.fields['data'].widget.attrs['class'] = 'form-control'
    self.fields['data'].widget.attrs['placeholder'] = 'Digite a data'
    
    self.fields['email'].widget.attrs['class'] = 'form-control'
    self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'


class Livro(forms.ModelForm):
  class Meta:
    model = Livros
    fields = '__all__'
