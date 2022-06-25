from django.urls import path

from . import views

app_name = 'chessapp'
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('', views.index, name='index'),
    path('<int:game_id>/', views.game, name='game'),
]