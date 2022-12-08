from django.db import models
from phonenumber_field.modelfields import PhoneNumber
import phonenumbers
# Create your models here.

class Service(models.Model):
    image = models.ImageField(upload_to='website/', blank=True, null=True)
    title = models.CharField(max_length=155)
    content = models.TextField()
    
    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=20)
    content = models.TextField()
    email = models.EmailField(max_length=219)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} -- {self.email}'

    class Meta:
        verbose_name = 'букинг'
        verbose_name_plural = 'букинги'