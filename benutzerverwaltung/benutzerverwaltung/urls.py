from django.conf.urls import url, include
from django.contrib import admin
from benutzerverwaltung import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^user/', include('benutzeraccounts.urls', namespace='user')),
    url(r'^assets/', include('benutzeraccounts.urls', namespace='assets')),
]
