from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view),
    path('test/', views.home_view),
]
