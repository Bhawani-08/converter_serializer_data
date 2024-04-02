from django.db import models

# Create your models here.

class Table1(models.Model):
    name = models.CharField(max_length = 30)
    class1 = models.IntegerField()


class Table2(models.Model):
    sub = models.CharField(max_length = 20)  
    roll_no = models.IntegerField(primary_key = True)

