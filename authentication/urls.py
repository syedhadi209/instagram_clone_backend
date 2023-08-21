from django.urls import path
from .views import RegisterUser,LoginUser,GetUserData


urlpatterns = [
    path('signup/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
    path('get-user/', GetUserData.as_view())
]