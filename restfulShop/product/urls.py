from .views import *
from  django.urls import path

urlpatterns = [    
    path('', ProductListApiView.as_view()),
    path('<int:pk>', ProductListApiView.as_view()),
    path('create', ProductCreateApiView.as_view()),
    path('update/<int:pk>', ProductUpdateApiView.as_view()),
]