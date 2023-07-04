from rest_framework import serializers
from .models import *

class CommentSerializer(serializers.ModelSerializer):            # 댓글 시리얼라이저
    class Meta:
        model=Comment
        fields=['id','post','author','content','created_at']


class PostSerializer(serializers.ModelSerializer):               # 게시글 시리얼라이저
    comment=CommentSerializer(many=True, read_only=True)        #중첩 시리얼라이저 1:N관계
    class Meta:
        model=Post
        fields=['id','title','author','content','created_at','comment']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','username','email','password']
    def create(self, validated_data): # 회원정보가 save될 때 원래 create가 쓰일것임 그때 set_password라는 기능을 추가한 느낌
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128,write_only=True)

    def validate(self, data):
        email = data.get("email",None)
        password = data.get("password",None)

        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError()
            else:
                return user