from django.shortcuts import render, HttpResponse

def principal1(request):
    return render (request,"inicio/principal1.html")    

def contacto(request):
  
    return render(request,"inicio/contacto.html")  

def formulario(request):
    return render(request,"inicio/formulario.html")


def ejemplo(request):
    return render(request,"inicio/ejemplo.html") 
   

