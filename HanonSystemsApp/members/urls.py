from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="Login"),
     path('logout_user', views.logout_user, name='Logout'),
]