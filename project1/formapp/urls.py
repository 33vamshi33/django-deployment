from django.conf.urls import url
from django.urls import path
from formapp import views

urlpatterns = [
    path('',views.formnameview,name="forms"),
]
