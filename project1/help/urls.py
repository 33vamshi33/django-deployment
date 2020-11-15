from django.conf.urls import url
from help import views

urlpatterns = [
    url(r'^$',views.users,name="help-page"),
]



