from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:year>', views.name),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
]
