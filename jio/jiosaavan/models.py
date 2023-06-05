from django.db import models

# Create your models here.
class product(models.Model):
    Name= models.CharField(max_length=30)
    Desc= models.CharField(max_length=300)
    Cost= models.IntegerField()

class registration(models.Model):
    Name= models.CharField(max_length=30, default='')
    Age= models.IntegerField()
    Email= models.CharField(max_length=100, default='')
    Password= models.CharField(max_length=20, default='')
    def __str__(self) -> str:
        return self.Name