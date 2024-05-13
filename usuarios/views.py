from django.shortcuts import redirect, render
from django.http import HttpResponse
from hashlib import sha256

from usuarios.models import Usuario

def cadastro(request):
  return render(request, 'cadastro.html')

def valida_cadastro(request):
  nome = request.POST.get('nome')
  email = request.POST.get('email')
  senha = request.POST.get('senha')
  usuario_existe = Usuario.objects.filter(email=email)

  if len(nome.strip()) == 0 or len(email.strip()) == 0:
    return redirect('/auth/cadastro/?status=1')
  if len(senha.strip()) < 6:
    return redirect('/auth/cadastro/?status=2')
  if usuario_existe:
    return redirect('/auth/cadastro/?status=3')
    
  senha = sha256(senha.encode()).hexdigest()
  
  try:
    novo_usuario = Usuario(nome=nome, email=email, senha=senha)
    novo_usuario.save()
    return redirect('/auth/cadastro/?status=0')
  except:
    return redirect('/auth/cadastro/?status=4')
  
def login(request):
  return render(request, 'login.html')