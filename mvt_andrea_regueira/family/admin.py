from django.contrib import admin
from family.models import Family_people

# admin.siteregister(family_people) Ese no va, lo corregimos
# Te faltaba un puntito ahi en el de arriba
# Register your models here.

# admin.siteregister(family_people)
admin.site.register(Family_people)