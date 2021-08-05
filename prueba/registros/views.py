from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Alumnos, Archivos
from .forms import ComentarioContactoForm
from .models import ComentarioContacto
from .forms import FormArchivos
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
import datetime


def consultariosComentarioContacto(request):
    comentarios = ComentarioContacto.objects.all()

    return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})




def principal(request):
    alumnos=Alumnos.objects.all()

    return render(request,"registros/principal1.html",{'alumnos':alumnos})


def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera="TIC")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera="BIO").filter(turno="Vespertino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consultar3(request):
    alumnos=Alumnos.objects.all().only('matricula','nombre','carrera','turno','imagen')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Ves")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})
def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
   fechaIinicio = datetime.date(2021, 7, 1)
   fechaFin = datetime.date(2021, 7, 16)
   alumnos=Alumnos.objects.filter(created__range=(fechaIinicio,fechaFin))
   return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
   
   alumnos=Alumnos.objects.filter(comentario__comment='Se confia mucho para la entrega de las clases')
   return render(request,"registros/consultas.html",{'alumnos':alumnos})



def eliminarComentarioContacto(request, id,
    confirmacion = 'registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method== 'POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaContacto.html",
              {'comentarios':comentarios})
    
    return render(request, confirmacion, {'object':comentario})


def consultarComentarioIndiviual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    return render(request,'registros/formEditarComentario.html',{'comentario':comentario})

def editarComentarioContacto(request,id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()
            return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})

    return render(request,"registros/formEditarComentario.html",{'comentario':comentario})         






def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
                form.save()
                comentarios = ComentarioContacto.objects.all()
                return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
    form = ComentarioContactoForm()

    return render(request, 'registros/contacto.html',{'form':form})


def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html", {'nombre': nombre})


def contacto(request):
    return render(request,"registros/contacto.html")


def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula,nombre, carrera, turno, imagen from registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
                titulo = request.POST['titulo']
                descripcion = request.POST['descripcion']
                archivo = request.FILES['archivo']
                insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
                form.save()
                return render(request,"registros/archivos.html")
        else:
                messages.error(request, "Error al procesar el formulario")
    else:
     return render(request, 'registros/archivos.html',{'archivo':Archivos})



