from django.conf.urls import url
from Registration import views

#TEMPLATE TAGGING
app_name = 'registration'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^students/$', views.list, name='list'),
    url(r'^form/$', views.user_entry, name='form'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
