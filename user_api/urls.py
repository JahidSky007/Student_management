from django.urls import path

from user_api import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='user-login'),
]
