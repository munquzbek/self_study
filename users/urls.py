from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView

app_name = UsersConfig.name

urlpatterns = [
    #  user CreateReadUpdateDelete(CRUD)
    path('signup/', UserCreateAPIView.as_view(), name='user-register'),
    path('list/', UserListAPIView.as_view(), name='user-list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user-delete'),
]
