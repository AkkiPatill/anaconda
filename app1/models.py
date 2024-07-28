from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    phone = models.BigIntegerField(unique=True, null=True, blank=True)
    pincode = models.IntegerField(null=True)


    class Meta:
        db_table = "employee"

        def __str__(self) -> str:
            return self.name
        

