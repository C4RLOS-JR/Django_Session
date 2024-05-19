from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
  if request.session.get('logado'): # tenta pegar a sessionid do usuário.
    return render(request, 'home.html', {'logado': request.session['logado']})
  else:
    messages.add_message(request, constants.WARNING, 'Você precisa estar logado para acessar a plataforma!')
    return redirect('/auth/login/')