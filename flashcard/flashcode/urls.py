from django.urls import path
from . import views

urlpatterns = [
    path('', views.cards , name="cards"),
    path('card_data/<str:pk>/', views.card_data , name="card_data"),
    
]