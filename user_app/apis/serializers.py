from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({"Passwords dosen't matched"})
        
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'Email already exists!'})
        
        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'Username already exists try another username!'})
        
        
        
        account=User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account