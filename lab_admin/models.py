from django.db import models

# Create your models here.
class signup_info(models.Model) :
    full_name = models.CharField(max_length=30)
    roll_no= models.CharField(max_length=30)
    batch = models.CharField(max_length=30)
    phone_no= models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password= models.CharField(max_length=30)


    def __str__(self):
        return self.full_name

class ticket(models.Model) :
    name = models.CharField(max_length=30)
    roll_no= models.CharField(max_length=30)
    pc_number = models.CharField(max_length=30)
    problem= models.CharField(max_length=200)