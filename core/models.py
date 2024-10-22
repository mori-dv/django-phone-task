from django.db import models

from .utils.validators import validate_positive


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Phone(models.Model):

    class Status(models.TextChoices):
        exist = "Eٍ", "Exist"
        notExist = "N", "NotExist"

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones')
    model = models.CharField(max_length=100, unique=True)
    price = models.PositiveIntegerField(validators=[validate_positive])
    color = models.CharField(max_length=50)
    screen_size = models.FloatField(validators=[validate_positive])
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.exist)
    country_of_manufacture = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.brand.name} {self.model}"
