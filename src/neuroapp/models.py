from django.db import models


# Create your models here.
class TestImage(models.Model):
    name = models.CharField("Название", max_length=40)
    image = models.ImageField('Фото', upload_to='')
