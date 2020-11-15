from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic,Webpage,AccessRecord


# Create your views here.

def index(request):
    # return HttpResponse("<em>hello world</em>")
    my_dict={'insert_me':"hello I am from views.py  "}

    #orderby in sql
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}


    return render(request,"app1/index.html",context=date_dict)
    #return HttpResponse("hello") to print hello

def base(request):
    context_dict={'name':"VamsHi Krishna",'number':100}
    return render(request,"app1/base.html",context=context_dict);

def releative(request):
    return render(request,"app1/releativeurltemplate.html")