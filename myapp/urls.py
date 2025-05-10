
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # OR views.home — just one
    path('2/', views.page2, name='page2'),
    path('3/', views.page3, name='page3'),
]




