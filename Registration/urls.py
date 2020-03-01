from django.conf.urls import url
from Registration import views

urlpatterns = [
    url('', views.index, name='list'),
]
