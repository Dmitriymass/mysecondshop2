from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^users/$', views.users, name='users'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.user_stat, name='user_stat'),
]
