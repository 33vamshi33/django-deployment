from django.shortcuts import render
from formapp import forms
# Create your views here.

#just for test le
# def index(request):
#     return render(request,"formapp/index.html")


def formnameview(request):
    form=forms.formname()

    if request.method=='POST':
        form=forms.formname(request.POST)

        if form.is_valid():
            #add to database
            print("vadilation success")
            print("name is "+form.cleaned_data['name'])
            print("email is "+form.cleaned_data['email'])
            print("text is "+form.cleaned_data['text'])


    return render(request,"formapp/index.html",{'form':form})