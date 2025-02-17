from django.db import models

# Create your models here.

class Profile(models.Model):

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=45)
    roll = models.IntegerField()
    marks = models.FloatField()
    admit_date = models.DateTimeField(null=True)


    def __str__(self):
        return f"{self.fname} {self.lname}"