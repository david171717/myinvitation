from django.conf.urls import url, include
from . import views
from .forms import SignupForm, LoginForm
from home.forms import LoginForm
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup_ok/$', views.signup_ok, name='signup_ok'),
    # url(r'^login/$', views.loginview, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'home/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logoutview, name='logout'),
    # url(r'^logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),
    url(r'^invitation/$', views.invitation, name='invitation'),
]