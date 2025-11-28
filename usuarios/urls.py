from django.urls import path
from usuarios.views import iniciar_sesion, registro
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView 

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(next_page='logout-mensaje'), name='cerrar_sesion'),
    path('logout-mensaje/', TemplateView.as_view(template_name='cerrar_sesion.html'), name='logout-mensaje'),
    path('registro/', registro, name='registro'),
]

