from django.urls import path
from . import views

#api request urls
urlpatterns = [
    path('card_list', views.cards , name="card_list"),
    path('card_data/<str:pk>/', views.card_data , name="card_data"),
    path('card_create/', views.card_create , name="card_create"),
    path('card_update/<str:pk>', views.card_update , name="card_update"),
    path('card_delete/<str:pk>', views.card_delete , name="card_delete"),
    path('card_remember/<str:pk>', views.card_remember , name="card_remember"),
]