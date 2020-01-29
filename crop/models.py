from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime

# Create your models here.
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
 
class Crate(models.Model):
    country =CountryField(default = 'Kenya')
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    
    def __str__(self):
       return self.country


class Sample(models.Model):
    crate = models.ForeignKey(Crate)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    batch_number = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    receipt_date = models.DateField()
    archival_date = models.DateTimeField(auto_now_add=True)
