from django.urls import path ,include
from . import views

urlpatterns = [
    path('/ramanacho', views.xd),
    path('/oe', views.oe)
]