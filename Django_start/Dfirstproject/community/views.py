from django.shortcuts import render,get_object_or_404

from community.models import Posting
from django.utils import timezone
from django.db.models import Q



# Create your views here.

def List(request):
    posts=Posting.objects.filter(upload_time__lte=timezone.now()).order_by('upload_time') #lte: less than equal
    return render(request,'list.html',{'posts':posts})

def detail(request,pk):
    post= get_object_or_404(Posting,pk=pk)
    return render(request,'detail.html',{'post':post})

def search(request):
  search=request.GET.get('search','')   #request는 Get
  #search = request.GET['search']
  #print(request)
  #print(search)
  #postf=Posting.objects.filter(title__icontains = search) 제목만 필터링
  postf=Posting.objects.filter(
     Q(title__icontains = search) | Q(content__icontains = search)
  )
  #print(postf)
  return render(request, 'search.html',{'postf':postf})
