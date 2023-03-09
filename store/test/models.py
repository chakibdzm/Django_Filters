from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=150)
    tagline=models.TextField()
    description=models.CharField(max_length=250)
    price=models.IntegerField()

    def __str__(self):
        return self.name
class Collection(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    


