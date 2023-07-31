from django.urls import path
from . import views

urlpatterns = [
    path('lobby/', views.lobby, name='lobby'),
]


#path('edit/', views.edit, name='edit'),