from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from api import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include(
        'rest_framework.urls'
        )
    ),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>/', views.GameDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('runic_game_action/<str:game_hash>', views.GameMaster.as_view()),
    path('new_game/', views.GameUrl.as_view()),
    path('users/register', views.CreateUserView.as_view())
]
