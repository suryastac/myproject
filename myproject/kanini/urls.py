from django.urls import path

from kanini import views

urlpatterns = [
    path('',views.index,name='index'),
]
