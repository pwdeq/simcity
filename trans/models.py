from django.db import models
from django.contrib.auth.models import User


class ticket(models.Model):
    category = models.CharField(max_length=100)
    nickname = models.CharField(max_length=40)
    nickname2 = models.CharField(max_length=40)
    chip_count =models.CharField(max_length=40)
    transfered_chip_count = models.DecimalField(max_digits=10, decimal_places=2)
    create_date = models.DateTimeField()
    action = models.CharField(max_length=40)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    approve = models.CharField(max_length=40)
    decline = models.CharField(max_length=40)