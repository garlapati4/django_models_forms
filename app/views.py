from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFOD=TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse('Topic_name is created')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    WPMFO=WebpageModelForm()
    d={'WPMFO':WPMFO}
    if request.method=='POST':
        WPMFOD=WebpageModelForm(request.POST)
        if WPMFOD.is_valid():
            WPMFOD.save()
            return HttpResponse('Webpage is created')
    return render(request,'insert_webpage.html',d)
def insert_access(request):
    ARMFO=AccessRecordModelForm()
    d={'ARMFO':ARMFO}
    if request.method=='POST':
        ARMFOD=AccessRecordModelForm(request.POST)
        if ARMFOD.is_valid():
            ARMFOD.save()
            return HttpResponse('AccessRecord is created')
    return render(request,'insert_access.html',d)