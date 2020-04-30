from django.db import models

class DjangoDemo(models.Model):
  a_asset_id = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
  ad_client_id = models.DecimalField(max_digits=10, decimal_places=0)
  ad_org_id = models.DecimalField(max_digits=10, decimal_places=0)
  isactive = models.CharField(max_length=1)
