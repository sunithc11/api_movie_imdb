from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from api.models import WatchList,StreamPlatform,Review
from api.apis.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework import mixins
from rest_framework import generics,filters
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from api.apis.permissions import ISReviewUserorReadOnly,IsAdminorReadOnly
from rest_framework.permissions import IsAuthenticated
from api.apis.throtting import (ReveiwCreateThrottle,ReveiwListThrottle,ReveiwDetailsThrottle,
                                StreamPlatformListThrottle,StreamPlatformDetailsThrottle,
                                WatchListThrottle,WatchDetailsThrottle)
from api.apis.pagination import LoSung,LoSuuung
from rest_framework.throttling import AnonRateThrottle



#Review
class ReviewCreateAV(generics.CreateAPIView):
    serializer_class=ReviewSerializer   
    permission_classes=[ISReviewUserorReadOnly]
    throttle_classes=[ReveiwCreateThrottle]
    filter_backends=[filters.SearchFilter]
    search_fields=['review_user__username']
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self,serializer):
        pk=self.kwargs.get('pk')
        watchlist=WatchList.objects.get(pk=pk)
        
        review_user=self.request.user
        review_queryset=Review.objects.filter(watchlist=watchlist,review_user=review_user)
        
        if review_queryset.exists():
            raise ValidationError("Already reviewed to the Movie!")
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating + serializer.validated_data['rating'])/2
            
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

    
        serializer.save(watchlist=watchlist,review_user=review_user)
    
    
class ReviewListAV(generics.ListAPIView):
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    throttle_classes=[ReveiwListThrottle]
    filter_backends=[filters.SearchFilter]
    search_fields=['review_user__username']
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ISReviewUserorReadOnly]
    throttle_classes=[ReveiwDetailsThrottle]
    filter_backends=[filters.SearchFilter]
    search_fields=['review_user__username']
    
    
    def get_object(self):
        watchlist_id = self.kwargs['entity_pk']
        review_id = self.kwargs['review_pk']
        return Review.objects.get(watchlist_id=watchlist_id, id=review_id)
    
class ReviewList(generics.ListAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAuthenticated]
    throttle_classes=[ReveiwListThrottle]
    filter_backends=[filters.SearchFilter]
    search_fields=['review_user__username']
    pagination_class=LoSuuung

class ReviewDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[ISReviewUserorReadOnly]
    throttle_classes=[ReveiwDetailsThrottle]
    filter_backends=[filters.SearchFilter]
    search_fields=['review_user__username']
    
    
    

   
#StreamPlatform
# class StreamPlatformListAV(APIView):
#     def get(self,request):
#         platform=StreamPlatform.objects.all()
#         ser=StreamPlatformSerializer(platform,many=True)
#         return Response(ser.data)
        
            
#     def post(self,request):
#         ser=StreamPlatformSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         else:
#             return Response(ser.errors)
    
    
#     def delete(self,request):
#         platform=StreamPlatform.objects.all()
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
        
        
# class StreamPlatformDetailsAV(APIView):
#     def get(self,request,pk):
#         platform=StreamPlatform.objects.get(pk=pk)
#         ser=StreamPlatformSerializer(platform)
#         return Response(ser.data)
                            
            
#     def put(self,request,pk):
#         platform=StreamPlatform.objects.get(pk=pk)
#         ser=StreamPlatformSerializer(platform,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         else:
#             return Response(ser.errors)
        
        
#     def patch(self,request,pk):
#         platform=StreamPlatform.objects.get(pk=pk)
#         ser=StreamPlatformSerializer(platform,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         else:
#             return Response(ser.errors)
        
#     def delete(self,request,pk):
#         platform=StreamPlatform.objects.get(pk=pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# class StreamPlatformAV(viewsets.ModelViewSet):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
#     permission_classes = [IsAdminorReadOnly]
    
    
class StreamPlatformListAV(generics.ListAPIView):
    queryset=StreamPlatform.objects.all().order_by('id')
    serializer_class=StreamPlatformSerializer
    permission_classes=[IsAdminorReadOnly]
    throttle_classes=[AnonRateThrottle]
    # pagination_class=LoSuuung
    # filter_backends=[filters.SearchFilter]
    # search_fields=['name']
    

class StreamPlatformDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=[IsAdminorReadOnly]
    throttle_classes=[AnonRateThrottle]
    # filter_backends=[filters.SearchFilter]
    # search_fields=['name']
    
    # def list(self, request):
    #     queryset = StreamPlatform.objects.all()
    #     serializer = StreamPlatformSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk):
    #     queryset = StreamPlatform.objects.get(pk=pk)
    #     #user = get_object_or_404(queryset, pk=pk)
    #     serializer = StreamPlatformSerializer(queryset)
    #     return Response(serializer.data)
    
    
    
#WatchList
class WatchListAV(generics.ListAPIView):
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer
    permission_classes=[IsAdminorReadOnly]
    throttle_classes=[WatchListThrottle]
    filter_backends=[filters.SearchFilter]
    search_fields=['platform__name']
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['avg_rating']
    pagination_class=LoSung

class WatchDetailsAV(generics.RetrieveUpdateDestroyAPIView):
    queryset=WatchList.objects.all()
    serializer_class=WatchListSerializer
    permission_classes=[IsAdminorReadOnly]
    throttle_classes=[WatchDetailsThrottle]
    filter_backends=[filters.SearchFilter]
    search_fields=['platform__name']
    
# class WatchListAV(APIView):
#     permission_classes = [IsAdminorReadOnly]
#     throttle_classes=[WatchListThrottle]
#     def get(self,request):
#         movies=WatchList.objects.all()
#         ser=WatchListSerializer(movies,many=True)
#         return Response(ser.data)
        
            
#     def post(self,request):
#         ser=WatchListSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         else:
#             return Response(ser.errors)
    
    
#     def delete(self,request):
#         movies=WatchList.objects.all()
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)    
        
        
# class WatchDetailsAV(APIView):
#     permission_classes = [IsAdminorReadOnly]
#     throttle_classes=[WatchDetailsThrottle]
#     def get(self,request,pk):
#         movies=WatchList.objects.get(pk=pk)
#         ser=WatchListSerializer(movies)
#         return Response(ser.data)
                            
            
#     def put(self,request,pk):
#         movies=WatchList.objects.get(pk=pk)
#         ser=WatchListSerializer(movies,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         else:
#             return Response(ser.errors)
        
        
#     def patch(self,request,pk):
#         movies=WatchList.objects.get(pk=pk)
#         ser=WatchListSerializer(movies,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         else:
#             return Response(ser.errors)
        
#     def delete(self,request,pk):
#         movies=WatchList.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
# #Review 
# class ReviewListAV(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
    
# class ReviewDetailsAV(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)