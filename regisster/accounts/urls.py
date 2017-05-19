
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from accounts.views import Home,front

urlpatterns = [
	url(r'^front/$',front.as_view(),name='front'),
	url(r'^home/$',Home.as_view(),name='home'),
	url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
	url(r'^login/$', auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    
]