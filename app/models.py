from django.db import models

class Mydb(models.Model):
 name = models.CharField(max_length=50)
 age = models.IntegerField()
 address = models.TextField()
 mobile = models.IntegerField()
