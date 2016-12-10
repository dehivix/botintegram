# -*- coding: utf-8 -*-
from django import forms
from django.shortcuts import render_to_response
from general.models import Personas
from django.forms.util import ErrorList, ErrorDict
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


"""
Formulario para el registro de nuevas cuentas
"""

class registro_usuario(forms.Form):
    cedula = forms.CharField(max_length=30, label=u'Cédula', widget=forms.TextInput(attrs={'type':'text', 'class':'text', 'autofocus':'autofocus', 'required':'required', 'value':''}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type':'text', 'class':'text', 'autofocus':'autofocus', 'required':'required', 'value':''}))
    password1 = forms.CharField(max_length=10, label=u"Contraseña", widget=forms.PasswordInput(attrs={'type':'password', 'class':'password', 'autofocus':'autofocus', 'required':'required', 'value':''}))
