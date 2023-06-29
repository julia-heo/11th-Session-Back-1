from django.contrib import admin
from django.urls import path
from .views import *

app_name='api'                  # app name작성 후 view와 url연결

urlpatterns = [
    path("posts/", PostListView.as_view()),
    path('posts/<int:pk>',PostDetailView.as_view()),
    path('comments/',CommentView.as_view()),
    path('comments/<int:pk>',CommentDetailView.as_view())
    
]


#class 함수는 as_view필요