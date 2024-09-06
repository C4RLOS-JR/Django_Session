from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .forms import Cliente
from .forms import Livro


@login_required(login_url='/auth/login')
def home(request):
  # if request.method == 'GET':
  #   form = Cliente()
  #   return render(request, 'home.html', {'form': form})
  # elif request.method == 'POST':
  #   form = Cliente(request.POST)
  #   if form.is_valid():
  #     nome = form.data['nome']
  #     idade = form.data['idade']
  #     data = form.data['data']
  #     email = form.data['email']
  #     form.cleaned_data

  #     messages.add_message(request, constants.SUCCESS, 'Formulário enviado com sucesso!')
  #     return redirect('home')

  #   return render(request, 'home.html', {'form': form})

  if request.method == 'GET':
    form = Livro()
    return render(request, 'home.html', {'form': form})
  elif request.method == 'POST':
    form = Livro(request.POST)
    if form.is_valid():
      form.save()
      form.cleaned_data
    return render(request, 'home.html', {'form': form})
