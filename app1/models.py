from django.db import models
# create sql table
# Create your models here.
class table1(models.Model):
    xAxis = models.CharField(max_length=200,default='DEFAULT VALUE')
    yAxis = models.CharField(max_length=200,default='DEFAULT VALUE')
class table2(models.Model):
    name = models.CharField(max_length=200,default='DEFAULT VALUE')
    prom = models.CharField(max_length=200,default='DEFAULT VALUE')
    prjm = models.CharField(max_length=200,default='DEFAULT VALUE')
    prod = models.CharField(max_length=200,default='DEFAULT VALUE')
