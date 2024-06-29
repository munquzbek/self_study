from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView

app_name = UsersConfig.name

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    #  user CreateReadUpdateDelete(CRUD)
    path('signup/', UserCreateAPIView.as_view(), name='user-register'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),

    #  token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
