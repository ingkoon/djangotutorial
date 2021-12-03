from django.urls import path
from .views import UserAPI, UserListAPI 

urlpatterns = [    
    path('api/User/UserList', UserListAPI.as_view()),
    path('api/User/', UserAPI.as_view()),
    path('api/User/<str:nickname>', UserAPI.as_view()),
]
