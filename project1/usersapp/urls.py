from django.urls import path
from django.conf.urls import url,include
from usersapp import views

app_name="usersapp"


urlpatterns = [
    path('',views.index,name="index"),
    path('registration/',views.registration,name="registration"),
    path('logout/',views.userlogout,name="userlogout"),
    path('special/',views.special,name="special"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('userlogout/',views.userlogout,name="userlogout"),
]
