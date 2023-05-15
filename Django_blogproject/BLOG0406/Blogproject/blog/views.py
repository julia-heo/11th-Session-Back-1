from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog, HashTag
from django.utils import timezone
from .forms import Blogform, Commentform

# Create your views here.

def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    blog_hashtag=blog_detail.hashtag.all()
    return render(request,'detail.html',{'blog':blog_detail,'hashtags':blog_hashtag})

def new(request): #이동하는 함수
    form=Blogform()
    return render (request,'new.html',{'form':form})

def create(request): #저장
    form=Blogform(request.POST,request.FILES)
    if form.is_valid(): #유효성 검사
        new_blog=form.save(commit=False)
        new_blog.date=timezone.now()
        new_blog.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(",")
        for tag in hashtag:
            # new_hashtag=HashTag()
            # new_hashtag.hashtag=tag
            # new_hashtag.save()
            # new_blog.hashtag.add(new_hashtag)
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_blog.hashtag.add(new_hashtag[0])
        return redirect ('detail',new_blog.id)
    return redirect('home')
    # new_blog=Blog()
    # new_blog.title=request.POST['title']
    # new_blog.body=request.POST['body']
    # new_blog.date=timezone.now()
    # new_blog.save()
    # return redirect('home')

def delete(request, blog_id):
    blog_delete=get_object_or_404(Blog,pk=blog_id)
    blog_delete.delete()
    return redirect('home')

def update_page(request,blog_id): #페이지 이동
    blog_update=get_object_or_404(Blog,pk=blog_id)
    return render(request,'update.html',{'blog':blog_update})

def update(request,blog_id):
    print(request)
    blog_update=get_object_or_404(Blog,pk=blog_id)
    blog_update.title=request.POST['title']
    blog_update.body=request.POST['body']
    blog_update.save()
    return redirect('home')

def add_comment(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)

    if request.method == 'POST':
        form = Commentform(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('detail',blog_id)
        
    else:
        form = Commentform()

    return render(request,'add_comment.html',{'form':form})