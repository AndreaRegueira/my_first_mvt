from django.db import models
from django.forms import CharField

# Create your models here.

class Family_people(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    profession = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Nombre: {self.name} | Apellido: {self.last_name} | Edad: {self.age} | Nacimiento: {self.date_of_birth} | Profesion: {self.profession}"
