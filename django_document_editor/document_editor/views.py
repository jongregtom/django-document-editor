# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime, json
import uuid

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from document_editor.models import Document


def index(request):
    template = loader.get_template('documents/index.html')
    documents = None #TODO: fetch documents after model created
    context = {'documents': documents}
    return HttpResponse(template.render(context, request))


def document_editor(request):
    template = loader.get_template('document_editor/index.html')
    document_id = None
    context = {'document': document_id}
    return HttpResponse(template.render(context, request))

@csrf_exempt
## @requires_csrf_token
def save_document(request):
    print(request.body)
    req_body = json.loads(request.body)
    print(req_body)
    id = req_body['id']
    print(id)
    content = req_body['content']
    print(content)
    if id is None:
        print('no ID')
        id = uuid.uuid4()
    pub_date = datetime.datetime.now()
    document = Document.objects.filter(id=id).first()
    print(document)
    if document:
        print('existing doc')
        document.content = content
        document.pub_date = pub_date
        document.save()
    else:
        print('new doc')
        document = Document(id=id, content=content, pub_date=pub_date)
        document.save()
    print(document.id)
    return render(request, 'document_editor/index.html')
