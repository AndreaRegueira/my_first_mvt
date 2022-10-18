from django.urls import path
from family.views import create_family_data 
from family.views import create_list_people

urlpatterns = [
    path('create_family_data/<str:name>/<str:last_name>/<int:age>/<str:date_of_birth>/<str:profession>', create_family_data),
    path('list_family_people/', create_list_people),
]