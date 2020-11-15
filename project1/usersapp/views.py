from django.shortcuts import render
from usersapp.forms import userform,userprofileinfoform
from usersapp.models import userprofileinfo


#for login page
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
#from django.contrib.auth.decorators import reverse
from django.urls import reverse
#if we want to view to work when login required then below useful
from django.contrib.auth.decorators import login_required

# Create your views here.

def hello(request):
    return HttpResponse("hello page guys")

def index(request):
    return render(request,'usersapp/index.html')


@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('usersapp:index'))

@login_required
def special(request):
    return HttpResponse("you are logged in")

def registration(request):
    registered=False

    if request.method=='POST':
        user_form=userform(data=request.POST)
        profile_form=userprofileinfoform(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            #models lo em name use chesavo adi use cheyali 
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']

                profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)

    else:

        user_form=userform()
        profile_form=userprofileinfoform()

    return render(request,'usersapp/registration.html',{'registered':registered,
                                                        'user_form':user_form,
                                                        'profile_form':profile_form})

def userlogin(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('usersapp:index'))

            else :
                return HttpResponse("account not active")

        else :
            print("failed login")
            print("username is"+username)
            print("password is"+password)
            return HttpResponse("invalid login")

    else :
        return render(request,'usersapp/login.html')