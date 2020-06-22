
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^delete/$', views.delete_user, name='delete'),
    re_path(r'^insert/$', views.insert_user, name='insert'),
    re_path(r'^update/(?P<id>\d+)/$', views.update_user, name='update'),
    re_path(r'^users/$', views.users, name='users'),
    re_path(r'^user/(?P<id>\d+)/$', views.user, name='user')
]