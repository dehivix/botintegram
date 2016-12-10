# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin

class Personas(models.Model):
    cedula = models.CharField(max_length=8,unique=True,verbose_name=u'Número de Identificación')
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100,blank=True)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100,blank=True)
    genero = models.IntegerField(choices=((0,'Masculino'),(1,'Femenino')),default=0,verbose_name=u'sexo')
    direccion = models.TextField(verbose_name=u'dirección',blank=True)
    fecha_nacimiento = models.DateField()
    email = models.EmailField(blank=True)
    telf = models.CharField(max_length=11,blank=True,)
    membresia = models.ForeignKey('Iglesia')
    voto_activo = models.BooleanField()
    class Meta:
        db_table = u'personas'
        verbose_name_plural = "personas"
    def __unicode__(self):
        return u'%s %s %s'%(self.cedula,self.primer_apellido,self.primer_nombre)

class Cargos(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return  self.nombre
    class Meta:
        db_table = u'cargos'
        verbose_name_plural = 'cargos'


class Autoridades(models.Model):
    persona = models.ForeignKey('Personas',help_text=u'Ingrese el nombre, apellido o cédula de la persona que necesite consultar')
    cargos = models.ForeignKey(Cargos)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField()
    foto = models.ImageField(max_length=50, blank=True, null=True, verbose_name="Fotografia Digital", upload_to="fotos/")
    iglesia = models.ForeignKey('Iglesia',blank=True,default=0)
    class Meta:
        db_table = u'autoridades'
        #La combinación de estos campos no se puede repetir (django no acepta multiples primary keys)
        unique_together=('persona','cargos')
        verbose_name_plural="autoridades"
    def __unicode__(self):
        return u"%s" %(self.persona.persona)


class Iglesia(models.Model):
    nombre = models.CharField(max_length=100,)
    municipio=models.ForeignKey('Parroquia')
    class Meta:
        db_table=u'iglesia'
        unique_together=('nombre','municipio')
    def __unicode__(self):
        return self.nombre


class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        db_table = u'pais'
        verbose_name_plural='paises'
    def __unicode__(self):
        return "%s" % (self.nombre)


class Estado(models.Model):
    nombre = models.CharField(max_length=100,)
    pais = models.ForeignKey('Pais',verbose_name='país')
    class Meta:
        db_table = u'estado'
        verbose_name_plural='estados'
        unique_together=('nombre','pais')
    def __unicode__(self):
        return u'%s'%(self.nombre)

class Municipio(models.Model):
    nombre = models.CharField(max_length=100,)
    estado=models.ForeignKey('Estado')
    class Meta:
        db_table=u'municipio'
        unique_together=('nombre','estado')
    def __unicode__(self):
        return self.nombre


class Parroquia(models.Model):
    nombre = models.CharField(max_length=100,)
    municipio=models.ForeignKey('Municipio')
    class Meta:
        db_table=u'parroquia'
        unique_together=('nombre','municipio')
    def __unicode__(self):
        return self.nombre
