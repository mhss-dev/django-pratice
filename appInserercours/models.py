from django.db import models

# Create your models here.

class myCourses(models.Model):
    cours=models.CharField(max_length=60)
    formateur=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    heures=models.IntegerField()

    def __str__(self):
        return self.name