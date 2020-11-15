from django import forms
from django.core import validators

#check_for_z vadilator we bult it
def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("name needs to start with z")

class formname(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.EmailField()
    verify_email=forms.EmailField(label="enter your email again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,
            widget=forms.HiddenInput,
            validators=[validators.MaxLengthValidator(0)] #bultin validator
        )
    
    #write all clean functions in 1 function
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_email']

        if email !=vemail:
            raise forms.ValidationError("make sure both match")
    #bot catcher personal created one

    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher) >0:
            raise forms.ValidationError("found bot")
        return botcatcher


    #we have bultin validators that should be included in attributes


