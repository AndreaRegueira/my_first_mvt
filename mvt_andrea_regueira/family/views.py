from urllib import request
from django.shortcuts import render
from datetime import datetime

from family.models import Family_people

# Create your views here.

def create_family_data(resquet, name:str, last_name:str, age:int, date_of_birth:str, profession:str):
    date_of_birth = datetime.strftime(date_of_birth, "%Y-%m-%d")
    people = Family_people(name=name, last_name=last_name, age=age, date_of_birth=date_of_birth, profession=profession)
    people.save()

    context_dict = {'people' : people}
    return render(
        request=request,
        context=context_dict,
        template_name= 'family/create_family_data.html',
    )


def create_list_people(request):
    peoples = Family_people.objects.all()

    context_dict = {'peoples'} , {peoples}

    return render(
        request=request,
        context=context_dict,
        template_name='family/list_family_peoples.html',
    )

