from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', lambda request: redirect('/auth/login/')),
  path('auth/', include('usuarios.urls')),
  path('plataforma/', include('plataforma.urls'))
]
