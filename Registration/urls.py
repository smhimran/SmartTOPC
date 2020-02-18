from django.conf.urls import url
from Registration import views

urlpatterns = [
    url('', views.people, name='list'),
]
