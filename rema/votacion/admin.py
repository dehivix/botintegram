from django.contrib import admin
from models import Procesos
from models import Candidatos
from models import Votaciones
from models import VotoPersona

# Register your models here.
admin.site.register(Procesos)
admin.site.register(Candidatos)
admin.site.register(Votaciones)
admin.site.register(VotoPersona)
