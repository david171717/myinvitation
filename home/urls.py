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
    url(r'^login/$', auth_views.login, {'template_name': 'home/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),
    # url(r'^login/$', views.loginview, name='login'),
    # url(r'^logout/$', views.logoutview, name='logout'),
    url(r'^introduction/$', views.introduction, name='introduction'),
    url(r'^application/$', views.application, name='application'),
    url(r'^invitation/$', views.invitation, name='invitation'),
    url(r'^psjwedding/$', views.wedding, name='wedding'),
    url(r'^psjwedding/w_1$', views.w_1, name='w_1'),
    url(r'^psjwedding/w_2$', views.w_2, name='w_2'),
    url(r'^psjwedding/w_3$', views.w_3, name='w_3'),
    url(r'^psjwedding/w_4$', views.w_4, name='w_4'),
    url(r'^psjwedding/w_5$', views.w_5, name='w_5'),
    url(r'^psjwedding/w_6$', views.w_6, name='w_6'),
	# url(r'^wedding/w_1$', TemplateView.as_view(template_name="wedding/w_1.html"), name='w_1'),
    
]