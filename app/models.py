from django.db import models
from django.db import migrations

class studentData(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    age = models.CharField(max_length=2)
    mobile = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

class doctorData(models.Model):
    udn = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)

class parentData(models.Model):
    usn = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    parent = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)

class testData(models.Model):
    usn = models.CharField(max_length=100)
    test_name = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    advice = models.CharField(max_length=100)
    medicines = models.CharField(max_length=100)

class login(models.Model):
    usn = models.CharField(max_length=100)
    password = models.CharField(max_length=100)