from django.shortcuts import redirect, render
from django.http import HttpResponse

def home(request):
  if request.session.get('logado'): # tenta pegar a sessionid do usuário.
    return render(request, 'home.html', {'logado': request.session['logado']})
  else:
    return redirect('/auth/login/?status=7')