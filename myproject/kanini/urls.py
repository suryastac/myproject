from django.urls import path

from kanini import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    
]
