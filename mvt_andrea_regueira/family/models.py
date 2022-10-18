from django.db import models
# from unicodedata import name

from django.forms import CharField

# Create your models here.

class Family_people(models.Model): # En Python la primera letra de una clase es mayúscula
    name = models.CharField(max_length=30) # Ese MAX LENGHT aunque parezca parecido, no es igual a este que voy a poner ahora
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    date_of_birth = models.DateField()
    profession = models.CharField(max_length=30) # Faltaba el models.

    def __str__(self) -> str:
        return f"Nombre: {self.name} | Apellido: {self.last_name} | Edad: {self.age} | Nacimiento: {self.date_of_birth} | Profesion: {self.profession}"
