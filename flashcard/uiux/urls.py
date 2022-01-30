from django.urls import path
from . import views

#api request urls
urlpatterns = [
    path('', views.data , name="data")
]