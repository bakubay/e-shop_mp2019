from .views import *
from  django.urls import include, path

urlpatterns = [    
    path('', UserListApiView.as_view()),
    path('<int:pk>', UserApiView.as_view()),
    path('create', UserCreateApiView.as_view()),
    path('update/<int:pk>', UserUpdateApiView.as_view()),
]