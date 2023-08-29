from django.urls import path
from .views import *

urlpatterns = [
    path('follow/<followingUserId>/',FollowUser.as_view()),
    path('get-requests/', GetFollowRequests.as_view()),
    path('accept-request/<requestId>/', AcceptFollowRequest.as_view())
]