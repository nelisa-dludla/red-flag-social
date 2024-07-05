from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='results-index'),
    path('about/', views.about, name='results-about'),
]
