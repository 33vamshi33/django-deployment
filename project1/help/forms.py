from django import forms
from help.models import user


class userf(forms.Form):
    first_name=forms.CharField(max_length=264)
    last_name=forms.CharField(max_length=264)
    e_mail=forms.EmailField()


class newuser(forms.ModelForm):
    #inline validators

    class Meta:
        model=user
        fields="__all__"
