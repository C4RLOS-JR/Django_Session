from django.shortcuts import redirect, render
from django.http import HttpResponse
from hashlib import sha256
from .models import Usuario
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.contrib.auth.models import User

def cadastro(request):
  status = request.GET.get('status')
  return render(request, 'cadastro.html', {'status': status})

def valida_cadastro(request):
  nome = request.POST.get('nome')
  email = request.POST.get('email')
  senha = request.POST.get('senha')
  # usuario_existe = Usuario.objects.filter(email=email)

  if len(nome.strip()) == 0 or len(email.strip()) == 0:
    messages.add_message(request, constants.WARNING, 'Os campos "Nome" e "Email" não podem ficar em branco!')
    return redirect('/auth/cadastro/')
  if len(senha.strip()) < 6:
    messages.add_message(request, constants.WARNING, 'A senha tem que ter no mínimo 6 caracteres!')
    return redirect('/auth/cadastro/')
  # if usuario_existe:
  #   messages.add_message(request, constants.WARNING, 'Já existe um usuário cadastrado com esse Email!')
  #   return redirect('/auth/cadastro/')

  if User.objects.filter(email = email):
    messages.add_message(request, constants.WARNING, 'Já existe um usuário cadastrado com esse Email!')
    return redirect('/auth/cadastro/')
    
  try:
    # senha = sha256(senha.encode()).hexdigest()
    novo_usuario = User.objects.create_user(username = nome,
                                            email = email,
                                            password = senha)
    novo_usuario.save()
    messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
    return redirect('/auth/cadastro/')
  except:
    messages.add_message(request, constants.ERROR, 'Erro interno do sistema...tente novamente!')
    return redirect('/auth/cadastro/')
  
def login(request):
  status = request.GET.get('status')
  return render(request, 'login.html', {'status': status})

def valida_login(request):
  nome = request.POST.get('nome')
  senha = request.POST.get('senha')
  # senha = sha256(senha.encode()).hexdigest()
  usuario_existe = auth.authenticate(request, username = nome, password = senha)

  if not usuario_existe:
    messages.add_message(request, constants.ERROR, 'Usuário não cadastrado no sistema!')
    return redirect('/auth/login/')  
  
  # request.session['logado'] = True  # mostra se o usuário está logado.
  # request.session['usuario_id'] = usuario_existe[0].id  # mostra o ID do usuário que está logado.

  auth.login(request, usuario_existe)
  messages.add_message(request, constants.SUCCESS, f'Olá {usuario_existe.username}...Seja bem vindo(a)!')
  return render(request, 'home.html')

def sair(request):
  #return HttpResponse(request.session.get_expiry_date())
  # request.session.flush()  # deleta a session por completo.
  return redirect('/auth/login')