from django.db import models

# Create your models here.
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
