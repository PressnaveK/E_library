from django.urls import path
from . import views

urlpatterns = [
    path('About/<str:a>/<int:b>', views.functioncall, name="index")
]