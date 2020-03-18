from django.conf.urls import url
from Registration import views

urlpatterns = [
    url('', views.home, name='home'),
    url('students/', views.list, name='list'),
]
