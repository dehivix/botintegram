# -*- coding: utf-8 -*-
from django.db import models
from general.models import Cargos
from general.models import Autoridades
from general.models import Iglesia
from general.models import Personas

# Create your models here.
class Procesos(models.Model):
    cohorte = models.CharField(max_length=5,)
    fecha = models.DateField()
    iglesia = models.ForeignKey(Iglesia)
    estatus = models.BooleanField(True)
    class Meta:
        db_table=u'procesos'
        verbose_name_plural='procesos por periodo'
    def __unicode__(self):
        return "%s %s %s" % (self.iglesia.nombre, self.cohorte, self.fecha)


class Candidatos(models.Model):
    persona = models.ForeignKey(Personas,help_text=u'Ingrese el nombre, apellido o cédula de la persona que necesite consultar')
    cargos = models.ForeignKey(Cargos)
    proceso = models.ForeignKey(Procesos)
    fecha = models.DateField()
    descripcion = models.TextField(verbose_name=u'descripción del candidato', max_length=80, blank=True)
    foto = models.ImageField(max_length=50, blank=True, null=True, verbose_name="Fotografia Digital", upload_to="fotos/")
    iglesia = models.ForeignKey(Iglesia)
    class Meta:
        db_table = u'candidatos'
        unique_together=('persona','cargos')
        verbose_name_plural="candidatos"
    def __unicode__(self):
        return u"%s" %(self.persona)


class Votaciones(models.Model):
    proceso = models.ForeignKey(Procesos)
    candidato = models.ForeignKey('Candidatos')
    votos = models.IntegerField()
    gano = models.BooleanField(default=False)
    class Meta:
        db_table=u'votaciones'
        verbose_name_plural='votos del periodo'
    def __unicode__(self):
        return "%s %s %s - %s" % (self.proceso.iglesia.nombre, self.proceso.cohorte, self.cadidato.persona, self.votos)


class VotoPersona(models.Model):
    persona = models.ForeignKey(Personas)
    proceso = models.ForeignKey('Procesos')
    candidato = models.ForeignKey('Candidatos')
    class Meta:
        db_table=u'votopersona'
    def __unicode__(self):
        return "%s %s %s" % (self.proceso.iglesia.nombre, self.proceso.cohorte, self.candidato.persona)
