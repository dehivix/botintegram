from models import *
from django.contrib import admin
from django import forms
from django.contrib import messages

# Register your models here.
class PaisAdmin(admin.ModelAdmin):
    search_fields=['nombre']
admin.site.register(Pais,PaisAdmin)

class EstadoAdmin(admin.ModelAdmin):
    search_fields=['nombre','pais__nombre']
    list_display=('nombre','pais')
admin.site.register(Estado,EstadoAdmin)

class MunicipioAdmin(admin.ModelAdmin):
    search_fields=['nombre','estado__nombre','estado__pais__nombre']
    list_display=('nombre','estado')
admin.site.register(Municipio,MunicipioAdmin)

class ParroquiaAdmin(admin.ModelAdmin):
    search_fields=['nombre','municipio__nombre','municipio__estado__nombre','municipio__estado__pais__nombre']
    list_display=('nombre','municipio')
admin.site.register(Parroquia,ParroquiaAdmin)

class PersonasAdmin(admin.ModelAdmin):
    search_fields=['cedula']
    list_display=('cedula','primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido')
admin.site.register(Personas, PersonasAdmin)

admin.site.register(Cargos)
admin.site.register(Autoridades)
admin.site.register(Iglesia)
