import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')

import django
django.setup()

import random
from app1.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen=Faker()
topics=['search','Marketplace','News','Games','Science']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get topic for entry
        top=add_topic()

        #fake data for that entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #create new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        webpg.save()
        #create access record
        #here webpg means passing entire webpage for referncing due to foriegn key
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
        acc_rec.save()


if  __name__ == "__main__":
    print("populating")
    populate(20)
    print("completed")



