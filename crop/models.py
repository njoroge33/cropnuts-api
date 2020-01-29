from django.db import models
import datetime
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))
# Create your models here.

class Crate(models.Model):
    country = models.CharField(max_length=50)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    
    def __str__(self):
       return self.country  