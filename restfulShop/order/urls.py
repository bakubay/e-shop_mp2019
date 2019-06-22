from .views import *
from  django.urls import path

urlpatterns = [    
    path('<int:pk>', OrderApiView.as_view()),
    path('create', OrderCreateApiView.as_view()),
    path('update/<int:pk>', OrderUpdateApiView.as_view()),
]