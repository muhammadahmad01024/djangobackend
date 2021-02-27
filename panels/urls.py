from django.urls import path
from . import views

urlpatterns = [
    path('getPanels/', views.getPanels),
    path('saveComment/', views.saveComment),
    path('getComments/', views.getComments),
    path('deleteComment/', views.deleteComment),
    path('getPDF/', views.getPDF),
]
