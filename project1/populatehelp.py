import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django
django.setup()

from faker import Faker


fakegen=Faker()

from help.models import user




def populate(n):
    for i in range (n):
        fake_firstname=fakegen.first_name()
        fake_lastname=fakegen.last_name()
        fake_email=fakegen.ascii_email()

        t=user.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,e_mail=fake_email)[0]
        t.save()

if __name__=="__main__":
    populate(25)

