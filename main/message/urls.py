from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="message-home"),
  path('profile/', views.profile, name="message-profile"),
]