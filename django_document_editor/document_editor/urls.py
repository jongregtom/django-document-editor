from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit', views.document_editor, name='document_editor'),
    path('save_document', views.save_document, name='save_document')
]