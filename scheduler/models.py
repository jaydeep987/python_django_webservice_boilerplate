from django.db import models

class Schedule(models.Model):
  schedule_id = models.CharField(primary_key=True, max_length=20)
  client_id = models.CharField(max_length=20)
  cronpattern = models.CharField(max_length=10)
  frequency = models.DecimalField(max_digits=10, decimal_places=0)
  name = models.CharField(max_length=30)
  is_active = models.BooleanField()
