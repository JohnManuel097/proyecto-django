from django.contrib import admin 
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto
from .models import prubea

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula','nombre','carrera','turno')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    list_per_page=2
    list_display_links= ('matricula','nombre')
    list_editable=('turno',)
    def get_readonly_fields(self, request, obj: None):
        if request.user.groups.filter(name="Usuarios").exists():
            return ('matricula','carrera','turno')
        else:
            return ('created', 'updated')
admin.site.register(Alumnos,AdministrarModelo)

class AdministrarComentario(admin.ModelAdmin):
    readonly_fields=('created','id')
    list_display = ('id','comment')
    search_fields =('id','created')
    date_hierarchy = 'created'
    list_filter = ('created', 'id')
admin.site.register(Comentario, AdministrarComentario)



class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id','mensaje')
    readonly_fields=('created','id')
    search_fields =('id','created')
    date_hierarchy = 'created'


admin.site.register(ComentarioContacto, AdministrarComentariosContacto)


class Administrarprueba(admin.ModelAdmin):
    list_display = ('id','mensaje')
    readonly_fields=('created','id')
    search_fields =('id','created')
    date_hierarchy = 'created'


admin.site.register(prubea, Administrarprueba)

