from django.conf.urls import url
from Registration import views

#TEMPLATE TAGGING
app_name = 'registration'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^students/$', views.list, name='list'),
    url(r'^contestants/$', views.contestants, name='contestants'),
    url(r'^form/$', views.user_entry, name='form'),
    url(r'^register/$', views.register, name='register'),
    url(r'^reg_std/$', views.reg_std, name='reg_std'),
    url(r'^login/$', views.user_login, name='user_login'),
]
