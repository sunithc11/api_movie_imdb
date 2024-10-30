from django.urls import path
from api.apis.views import (WatchListAV,WatchDetailsAV,
                            ReviewListAV,ReviewCreateAV,ReviewList,ReviewDetails,
                            StreamPlatformListAV,ReviewDetailsAV,StreamPlatformDetailsAV)
#from api.apis.views import movie_details,movie_list

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


# router = DefaultRouter()
# router.register('stream', StreamPlatformAV, basename='stream')

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='watch-list'),
    path('list/<int:pk>/',WatchDetailsAV.as_view(),name='watch-item'),
    path('stream/',StreamPlatformListAV.as_view(),name='stream'),
    path('stream/<int:pk>/',StreamPlatformDetailsAV.as_view(),name='stream-details'),
    # path('',include(router.urls)),
    path('review/',ReviewList.as_view(),name='review'),
    path('list/<int:pk>/review/create/',ReviewCreateAV.as_view(),name='review-create'),
    path('list/<int:pk>/review/',ReviewListAV.as_view(),name='review-list'),
    path('list/review/<int:pk>/',ReviewDetailsAV.as_view(),name='review-item'),
    path('list/<int:entity_pk>/review/<int:review_pk>/',ReviewDetails.as_view(),name='review-lists'),
    #path('login/',obtain_auth_token,name='login'),
]