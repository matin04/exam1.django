from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField( max_length=100)
    quantity = models.CharField( max_length=150)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    photo = models.ImageField( upload_to='media', blank=True)
    video = models.ImageField( upload_to='media', blank=True)
    
    def __str__(self):
        return self.title
    