from rest_framework.decorators import api_view
from user_app.apis.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from user_app import models
from rest_framework.authtoken.models import Token

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    
@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data ={}
    
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registration Successful!'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED)