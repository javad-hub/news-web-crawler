from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('more/', views.more, name="more"),
    path('search/', views.search, name="search"),
]
