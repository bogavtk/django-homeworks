from django.urls import path
from lookup import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lookup/', views.lookup, name='lookup'),
]