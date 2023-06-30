from django.db import models


# Create your models here.

class details(models.Model):
    fullname = models.CharField(max_length=250)
    age = models.IntegerField()
    dob = models.IntegerField()
    gender = models.TextField()
    phone_number = models.IntegerField()
    email = models.TextField()
    address = models.TextField()
    department = models.TextField()
    course = models.TextField()

    def __str__(self):
        return self.name
