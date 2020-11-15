from django.shortcuts import render
from django.http import HttpResponse
from help.models import user
from help.forms import newuser,userf
# Create your views here.


formf=userf()

def index(request):
    return render(request,"help/signup.html",{'formf':formf})



def users(request):
    form=newuser()

    if request.method=="POST":
        form=newuser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("ok")
            return index(request)
        else:
            print("error invalid form")

    return render(request,"help/signup.html",{'form':form,'formf':formf})

