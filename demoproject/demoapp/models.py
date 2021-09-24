from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Product(models.Model):

    name=models.CharField(max_length=50)
    price=models.IntegerField()
    qty=models.IntegerField()


class Employee(models.Model):
    name=models.CharField(max_length=50)
    resume=models.FileField(upload_to='resume')






