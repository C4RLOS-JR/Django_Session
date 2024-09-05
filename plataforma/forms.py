from django import forms

class Cliente(forms.Form):
  nome = forms.CharField(max_length=30, required=False)
  idade = forms.IntegerField(required=False)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['nome'].widget.attrs['class'] = 'form-control'
    self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
    
    self.fields['idade'].widget.attrs['class'] = 'form-control'
    self.fields['idade'].widget.attrs['placeholder'] = 'Digite sua idade'
