from rest_framework import serializers
from api.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model =Review
        #fields='__all__'
        exclude=('watchlist',)
        
        
        
class WatchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model =WatchList
        fields='__all__'
        
        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist=WatchListSerializer(many=True,read_only=True)
    class Meta:
        model =StreamPlatform
        fields='__all__'
        
        
        

        
        
    # def validate_name(self,value):
    #     if len(value)<3:
    #         raise serializers.ValidationError("Movie name is too short!")
    #     else:
    #         return value
        
        
    # def validate(self,data):
    #     mv_name=WatchList.objects.all()
    #     movies=[i.name for i in mv_name]
    #     if data['name'] in movies:
    #         raise serializers.ValidationError("Movie name already exists")
    #     else:
    #         return data
    # id=serializers.IntegerField(read_only=True)
    # name=serializers.CharField()
    # desc=serializers.CharField()
    # rating=serializers.BooleanField()
    
    
    # def create(self,validated_data):
    #     return MovieList.objects.create(**validated_data)
    
    
    # def update(self,instance,validated_data):
    #     instance.name=validated_data.get('name',instance.name)
    #     instance.desc=validated_data.get('desc',instance.desc)
    #     instance.rating=validated_data.get('rating',instance.rating)
    #     instance.save()
    #     return instance
        