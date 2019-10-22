from django.urls import path

from . import views

app_name = 'gitrepos'
urlpatterns = [
    path('', views.index, name='index')
]
