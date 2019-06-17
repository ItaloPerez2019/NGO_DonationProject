from django.urls import path
from .views import UserListView,  UserCreateView, UserUpdateView, UserDeleteView


urlpatterns = [
    path('',UserListView.as_view() , name='user-list'),
    path('user/new/',UserCreateView.as_view() , name='user-create'),
    path('user/<int:pk>/update/',UserUpdateView.as_view() , name='user-update'),
    path('user/<int:pk>/delete/',UserDeleteView.as_view() , name='user-delete'),

]
