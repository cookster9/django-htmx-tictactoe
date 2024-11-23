from django.urls import path

from . import views

urlpatterns = [
    path('', views.startGame, name="startGame"),
    path('<int:pk>/', views.playGame, name='playGame'),
    path('<int:pk>/winner/', views.getWinner, name='getWinner'),
    path('games/', views.GameListView.as_view(), name='gameList'),
]