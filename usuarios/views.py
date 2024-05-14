from django.shortcuts import redirect, render
from django.http import HttpResponse
from hashlib import sha256

from usuarios.models import Usuario

def cadastro(request):
  status = request.GET.get('status')
  return render(request, 'cadastro.html', {'status': status})

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
    
  try:
    senha = sha256(senha.encode()).hexdigest()
    novo_usuario = Usuario(nome = nome,
                           email = email,
                           senha = senha)
    novo_usuario.save()
    return redirect('/auth/cadastro/?status=0')
  except:
    return redirect('/auth/cadastro/?status=4')
  
def login(request):
  status = request.GET.get('status')
  return render(request, 'login.html', {'status': status})

def valida_login(request):
  email = request.POST.get('email')
  senha = request.POST.get('senha')
  senha = sha256(senha.encode()).hexdigest()
  usuario_existe = Usuario.objects.filter(email=email)

  if not usuario_existe:
    return redirect('/auth/login/?status=5')
  if usuario_existe[0].senha != senha:
    return redirect('/auth/login/?status=6')
  
  request.session['logado'] = True
  return redirect('/plataforma/home')

def sair(request):
  request.session['logado'] = None
  return redirect('/auth/login')