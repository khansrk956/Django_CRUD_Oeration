from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    password = models.CharField(max_length=15,null=True)

    def __str__(self):
        return self.name
