from django.urls import path
from .views import RegisterUser,LoginUser,GetUserData,SearchUser,UpdateProfilePicture,GetProfileData,UpdateProfile


urlpatterns = [
    path('signup/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
    path('get-user/', GetUserData.as_view()),
    path('search/', SearchUser.as_view()),
    path('profile-update/', UpdateProfilePicture.as_view()),
    path('get-profile/', GetProfileData.as_view()),
    path('update-profile/',UpdateProfile.as_view())
]