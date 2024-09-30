from django.contrib import admin 
from . import views

urlpatterns = [
    path ("",views.hola,name="moras_clase_app"),
]
