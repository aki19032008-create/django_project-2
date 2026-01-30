from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_student, name='register'),
    path('start/', views.start_attendance, name='start'),
    path('attendance/', views.view_attendance, name='attendance'),
]