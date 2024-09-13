from django.urls import path
from . import views

urlpatterns = [
    path('vista1/', views.vista_1, name='vista_1'),
    path('vista2/', views.vista_2, name='vista_2'),
]
