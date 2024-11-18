from django.urls import path

from . import views

urlpatterns = [
    path("", views.startGame, name="startGame"),
    path('/<int:pk>/', views.playGame, name='playGame'),
]