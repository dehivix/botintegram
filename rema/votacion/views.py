# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.views import login
from django.contrib.auth import logout
from django.core.context_processors import csrf
from django.contrib.auth.models import User, Group
from django.views.decorators.csrf import csrf_protect
from django.contrib.sites.models import Site
import hashlib
from django.core.urlresolvers import reverse, NoReverseMatch
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db import models, IntegrityError
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.utils.http import base36_to_int
import datetime
from django.contrib.auth import authenticate
from forms import registro_usuario
from django.shortcuts import get_object_or_404
from models import Candidatos
from models import Procesos
from models import VotoPersona
from general.models import Personas

# Create your views here.
@csrf_protect
def index(request):
    if request.method == 'POST':
        form = registro_usuario(request.POST)
        if form.is_valid():
            email_user = form.cleaned_data['email']
            create_user = User.objects.create_user(username = email_user, email = email_user, password= pass_user)
            create_user.is_staff= False
            create_user.is_active=False
            create_user.save()
            return HttpResponseRedirect('/auth/enviado/')

    else:
        form = registro_usuario

    #import pdb;pdb.set_trace()
    from django.db.models import Q
    cedula = '20363511'
    persona = Personas.objects.get(cedula=cedula)
    proceso_activo = Procesos.objects.get(estatus=1)
    candidatos = Candidatos.objects.filter(proceso__pk=proceso_activo.pk, iglesia__pk=persona.membresia.pk)
    #candidatos_finales = []
    finales = []
    votos = VotoPersona.objects.filter(persona=persona, proceso=proceso_activo, candidato__in=candidatos)

    #finales = [ candidatos.exclude(Q(id=i.candidato.id) | Q(cargos=i.candidato.cargos) ) for i in votos ]

    candidatos_finales = candidatos.exclude(id__in=(votos))
    ya_voto = False
    '''try:
        candidatos_finales = finales.filter(cargos=finales[0].cargos)
    except:
        ya_voto = 'NO EXISTEN CANDIDATOS, O YA HA VOTADO POR TODOS LOS CARGOS'
    else:
        pass
    '''
    c = {}
    c.update(csrf(request))
    c.update({'form':form, 'candidatos': candidatos_finales, 'ya_voto': ya_voto})
    return render_to_response('index.html', c)
