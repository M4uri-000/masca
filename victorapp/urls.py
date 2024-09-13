from django.urls import path
from . import views

urlpatterns = [
    path('vista2/', views.vista_2),
    path('vista1/', views.vista_1),

]