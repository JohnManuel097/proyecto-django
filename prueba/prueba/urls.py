"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name, stat
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from inicio import views as p
from django.conf import settings
from registros import views
urlpatterns = [
    path('jet /' , include ( 'jet.urls')),
    path('jet /dashboard', include('jet.dashboard.urls','jet-dashboard')),
    path('admin/', admin.site.urls),
    path('',views.principal, name="principal1"),
    path('contacto/',views.contacto, name="Contacto"),
    path('formulario/',p.formulario, name="formulario"),
    path('ejemplo/',p.ejemplo, name="Ejemplo"),
    path('registrar/',views.registrar,name="Registrar"),
    path('consultarComentario/',views.consultariosComentarioContacto,name="Comentarios"),   
    path('eliminarComentario/<int:id>/',views.eliminarComentarioContacto,name="Eliminar"),  
    path('formEditarComentario/<int:id>/',views.consultarComentarioIndiviual,name="ConsultaIndividual"),
    path('editarComentario/<int:id>/',views.editarComentarioContacto,name="Editar"),  
    path('seguridad/',views.seguridad,name="Seguridad"),
    path('consultas1/',views.consultar1,name="Consultas"), 
    path('consultas2/',views.consultar2,name="Consultas2"), 
    path('consultas3/',views.consultar3,name="Consultas3"), 
    path('consultas4/',views.consultar4,name="Consultas4"), 
    path('consultas5/',views.consultar5,name="Consultas5"), 
    path('consultas6/',views.consultar6,name="Consultas6"),
    path('consultas7/',views.consultar7,name="Consultas7"), 
    path('consultasSQL/',views.consultasSQL,name="sql"), 
    path('subir',views.archivos,name="Subir"),
]

if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

