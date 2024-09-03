from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .forms import Cliente


@login_required(login_url='/auth/login')
def home(request):
  form = Cliente()
  return render(request, 'home.html', {'form': form})