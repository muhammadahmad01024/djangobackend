from django.urls import path
from . import views

urlpatterns = [
    path('getPanels/', views.getPanels),
]
